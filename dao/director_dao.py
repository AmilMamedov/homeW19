from app.dao.models.director import Director


class DirectorDAO:

    def __init__(self, session):
        """Получает сессию"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        return self.session.query(Director).all()

    def get_director_by_id(self, did: int) -> dict:
        """Получаем режиссера по id либо ошибка в str"""
        return self.session.query(Director).get(did)

    def add_director(self, data: dict):
        """Получаем json, добавляем нового режиссера в бд"""
        movie = Director(**data)
        self.session.add(movie)
        self.session.commit()

    def put_director(self, director: dict):
        """Обновляет режиссера"""
        self.session.add(director)
        self.session.commit()

        return director

    def delete_director(self, did: int):
        """Удаляем режиссера по id"""
        director = self.get_director_by_id(did)
        self.session.delete(director)
        self.session.commit()
