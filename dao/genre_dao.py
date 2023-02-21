from app.dao.models.genre import Genre
from app.setup_db import db


class GenreDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        return self.session.query(Genre).all()

    def get_genre_by_id(self, gid: int) -> dict:
        """Получаем жанр по id либо ошибка в str"""
        return self.session.query(Genre).get(gid)

    def add_genre(self, data: dict):
        """Получаем json, добавляем новый жанр в бд"""
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

    def put_genre(self, uid: int, genre: dict):
        """Обновляет жанр"""
        self.session.add(genre)
        self.session.commit()

    def delete_genre(self, gid: int):
        """Удаляем жанр по id"""
        director = self.get_genre_by_id(gid)
        self.session.delete(director)
        self.session.commit()
