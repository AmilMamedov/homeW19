from app.dao.genre_dao import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self) -> list[dict]:
        return self.dao.get_all()

    def add_genre(self, data: dict):
        return self.dao.add_genre(data)

    def put_genre(self, gid: int, data: dict):
        genre = self.get_genre_by_id(gid)

        if "name" in data:
            genre.name = data.get("name")

        self.dao.put_genre(genre)

    def get_genre_by_id(self, gid: int) -> dict:
        return self.dao.get_genre_by_id(gid)

    def delete_genre(self, gid: int):
        self.dao.delete_genre(gid)
