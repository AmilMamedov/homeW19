from flask_restx import Namespace, Resource
from flask import request

from app.container import director_service
from app.dao.models.director import DirectorSchema
from app.helpers.decorators import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """Получаем список всех режиссеров"""
        genres = director_service.get_all()
        return directors_schema.dump(genres), 200

    @admin_required
    def post(self):
        """Добавление режиссера"""
        req_json = request.json
        director_service.add_director(req_json)
        return f" Режиссер {req_json['name']} добавлен", 201


@director_ns.route('/<int:uid>')
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        """Возвращает режиссера по id"""
        genre = director_service.get_director_by_id(uid)
        return director_schema.dump(genre), 200

    @admin_required
    def put(self, uid):
        """Обновляет режиссера по id"""
        req_json = request.json
        print(type(req_json))
        director_service.put_director(uid, req_json)
        return f" Режиссер {req_json['name']} обновлен", 200

    @admin_required
    def delete(self, uid):
        """Удаляет режиссера по id"""
        director_service.delete_director(uid)
        return "", 204

