from app.dao.models.movie import Movie


class MovieDAO:

    def __init__(self, session):
        """Получает модель, схему и сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        return self.session.query(Movie).all()

    def get_film_by_id(self, fid: int) -> dict:
        """Получаем фильм по id либо ошибка в str"""
        return self.session.query(Movie).get(fid)

    def add_movie(self, data: dict):
        """Получаем json, добавляем новый фильм в бд"""
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def put_movie(self, movie: dict):
        """Обновляет фильм"""
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_film(self, fid: int):
        """Удаляем фильм по id"""
        movie = self.get_film_by_id(fid)
        self.session.delete(movie)
        self.session.commit()
