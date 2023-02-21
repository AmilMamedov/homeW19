from flask import request
from flask_restx import Namespace, Resource

from app.container import user_service
from app.dao.models.user import UserSchema
from app.helpers.decorators import admin_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    @admin_required
    def get(self):
        """Показывает всех юзеров"""
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        """регистрация нового юзера"""
        req_json = request.json
        user_service.add_new_user(req_json)
        return f" Пользователь {req_json['username']} добавлен", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def put(self, uid):
        """Обновление юзера по id"""
        req_json = request.json
        user_service.update_user(uid, req_json)
        return f" Пользователь {uid} обновлен", 201

    @admin_required
    def delete(self, uid):
        """Удаляем пользователя по id"""
        user_service.delete_user(uid)
        return "", 204


@user_ns.route('/<username>')
class UserView(Resource):
    @admin_required
    def get(self, username):
        """Получаем пользователя по username"""
        user = user_service.get_one_by_username(username)
        return user_schema.dump(user), 200
