import base64
import hashlib
import hmac

from app.dao.user_dao import UserDAO
from app.config import Config
from app.helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, uid: int) -> dict:
        return self.dao.get_one_by_id(uid)

    def get_one_by_username(self, username: str) -> dict:
        return self.dao.get_one_by_username(username)

    def add_new_user(self, data: dict):
        data["password"] = self.generated_password(data["password"])
        self.dao.add_new_user(data)

    def update_user(self, uid: int, data: dict):
        user = self.get_one_by_id(uid)
        user["password"] = self.generated_password(data["password"])
        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.username = data.get("password")
        if "role" in data:
            user.username = data.get("role")

        self.dao.update_user(user)

    def delete_user(self, uid: int):
        self.dao.delete_user(uid)

    def generated_password(self, password) -> bytes:
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """Принимаем хешированныйц пароль и строкой, сравниваем их. Возвращаем bool"""
        decode_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decode_digest, hash_digest)
