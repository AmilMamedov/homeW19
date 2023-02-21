from app.dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self) -> list[dict]:
        return self.dao.get_all()

    def add_director(self, data: dict):
        return self.dao.add_director(data)

    def put_director(self, did: int, data: dict):
        director = self.get_director_by_id(did)

        if "name" in data:
            director.name = data.get("name")

        self.dao.put_director(director)

    def get_director_by_id(self, did: int) -> dict:
        return self.dao.get_director_by_id(did)

    def delete_director(self, did: int):
        self.dao.delete_director(did)
