from app.dao.models.user import User


class UserDAO:

    def __init__(self, session):
        """Получает модель и схему"""
        self.session = session

    def get_all(self):
        """Получаем всех пользователей"""
        return self.session.query(User).all()

    def get_one_by_id(self, uid: int) -> dict:
        """Получаем юзера по id"""
        return self.session.query(User).get(uid)

    def get_one_by_username(self, username) -> dict:
        "Получаем юзера по username"
        return self.session.query(User).filter(User.username == username).first()

    def add_new_user(self, data: dict):
        """Получаем словарь, добавляем юзера"""
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update_user(self, user: dict):
        """Обновляем данные пользователя по id"""
        self.session.add(user)
        self.session.commit()

        return User

    def delete_user(self, uid: int):
        """Удаляем пользователя по id"""
        director = self.get_one_by_id(uid)
        self.session.delete(director)
        self.session.commit()


