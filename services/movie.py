from app.dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self) -> list[dict]:
        return self.dao.get_all()

    def add_movie(self, data: dict):
        return self.dao.add_movie(data)

    def put_movie(self, uid: int, data: dict):
        movie = self.get_film_by_id(uid)

        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "year" in data:
            movie.year = data.get("year")
        if "title" in data:
            movie.title = data.get("title")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "director_id" in data:
            movie.director_id = data.get("director_id")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "description" in data:
            movie.description = data.get("description")

        self.dao.put_movie(movie)

    def get_film_by_id(self, fid: int) -> dict:
        return self.dao.get_film_by_id(fid)

    def delete_film(self, fid: int):
        self.dao.delete_film(fid)
