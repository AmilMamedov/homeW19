import jwt
from flask import request, abort

from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    def wrapper(*args, **kwargs):
        #проверяем есть ли в заголовке запроса есть Authorization.
        if "Authorization" not in request.headers:
            abort(401)

        #Извлекаем токен
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        #пробуем декодировать токен с помощью секрета и алгоритма и вытаскиваем роль пользователя,
        #если роль не задана присваеваем user
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print("JWT DECODER Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        # проверяем есть ли в заголовке запроса есть Authorization.
        if "Authorization" not in request.headers:
            abort(401)
        # Извлекаем токен
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        role = None

        # пробуем декодировать токен с помощью секрета и алгоритма и вытаскиваем роль пользователя,
        # если роль не задана присваеваем user
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get("role", "user")
        except Exception as e:
            print("JWT DECODER Exception", e)
            abort(401)

        #проверяем требуемую роль
        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
