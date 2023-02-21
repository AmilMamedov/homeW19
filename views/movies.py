from flask_restx import Namespace, Resource
from flask import request

from app.container import movie_service
from app.dao.models.movie import MovieSchema
from app.helpers.decorators import auth_required, admin_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Получаем список всех фильмов"""
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    @admin_required
    def post(self):
        """Добавление фильма"""
        req_json = request.json
        movie_service.add_movie(req_json)
        return f" Фильм {req_json['title']} добавлен", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    @auth_required
    def get(self, uid):
        """Получаем фильм по id"""
        movie = movie_service.get_film_by_id(uid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, uid):
        """Обновление фильма по id"""
        req_json = request.json
        print(type(req_json))
        movie_service.put_movie(uid, req_json)
        return f" Фильм {req_json['title']} обновлен", 200

    @admin_required
    def delete(self, uid):
        """Удаление по id"""
        movie_service.delete_film(uid)
        return "", 204

