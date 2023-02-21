import calendar
import datetime


from flask_restx import abort
import jwt

from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM
from app.services.user import UserService


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, username, password, is_refresh=False):
        """Принимаем лони, пароль и наличие рефрешь токина и возвращаем новые токены"""
        #получаем юзера по нику
        user = self.user_service.get_one_by_username(username)

        #проверяем существование данного юзера
        if user is None:
            raise abort(404)

        #проверяем соответсвие паролей если это создание новых токенов
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        #30 minut for access token

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        acceess_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        #130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            "acceess_token": acceess_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        """Декодирум рефреш токен, извлекаем юзернейм и возвращаем новый токен"""
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get("username")

        return self.generate_token(username, None, is_refresh=True)


