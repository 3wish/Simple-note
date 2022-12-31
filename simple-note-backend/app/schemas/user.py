from passlib.context import CryptContext
from jose.exceptions import ExpiredSignatureError

from app.crud import user
from app.database.models import User
from .token import verify_token


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def hash_password(password):
    hashed_password = pwd_context.hash(password)
    return hashed_password


def verify_password(password: str, hashed_password: str) -> bool:
    local_hashed_password = hash_password(password)
    return pwd_context.verify(password, hashed_password)


def is_user_exist(username: str) -> User | bool:
    loca_user = user.get_user(username)
    return loca_user


def is_token_valid(token: str) -> dict | bool:
    try:
        result = verify_token(token)
    except ExpiredSignatureError as e:
        raise e
    return result


def store_user(username: str, password: str):
    hashed_password = hash_password(password)
    try:
        user.add_user(username, hashed_password)
    except Exception as e:
        print('Fail to add user with exception:\n', e)
        raise e

