from datetime import timedelta, datetime

from jose import JWTError, jwt
from jose.exceptions import ExpiredSignatureError

from app.crud import user

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(username: str, expires_delta: timedelta | None = None) -> str:
    if not expires_delta:
        expires_delta = datetime.now() + timedelta(days=1)

    payload: dict[str, timedelta] = {'sub': username, 'exp': expires_delta}
    token: str = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_token(token: str) -> dict | bool:
    try:
        payload: dict[str, int | str] = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except ExpiredSignatureError as e:
        raise e

    username = payload['sub']
    local_user = user.get_user(username)
    if local_user:
        return {'username': username, 'nickName': local_user.nick_name}
    else:
        return False
