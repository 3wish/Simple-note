from fastapi import APIRouter, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose.exceptions import ExpiredSignatureError

from app.schemas import user, token

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

oath2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class Token(BaseModel):
    accessToken: str
    tokenType: str


class RegisterInfo(BaseModel):
    username: str
    password: str


@router.post('/token')
async def get_access_token(is_keep: bool, form_data: OAuth2PasswordRequestForm = Depends()):
    username: str = form_data.username
    password: str = form_data.password

    local_user = user.is_user_exist(username)

    if not local_user:
        return {'code': 1001, 'msg': 'Incorrect username of password'}

    local_password: str = local_user.password

    if not user.verify_password(password, local_password):
        return {'code': 1001, 'msg': 'Incorrect username of password'}

    print(local_user.__dict__)

    if is_keep:
        user_token: str = token.create_token(username)
        return {'code': 1000,
                'msg': 'Login successfully',
                'data': {
                    'token': Token(accessToken=user_token, tokenType='Bearer'),
                    'profile': {
                        'username': local_user.username,
                        'nickName': local_user.nick_name
                    }
                }}
    else:
        return {'code': 1000,
                'msg': 'Login successfully',
                'data': {
                    'profile': {
                        'username': local_user.username,
                        'nickName': local_user.nick_name
                    }
                }}


@router.post('/register')
async def register_user(register_info: RegisterInfo):
    username = register_info.username
    password = register_info.password
    local_user = user.is_user_exist(username)

    if local_user:
        return {'code': 1002, 'msg': 'Existed user'}

    user.store_user(username, password)

    return {'code': 1000, 'msg': 'Register successfully'}


@router.get('/login')
async def get_user_by_token(usertoken: str = Depends(oath2_scheme)):
    try:
        result = user.is_token_valid(usertoken)
    except ExpiredSignatureError as e:
        return {'code': 1004, 'msg': 'Expired Token'}
    if result:
        return {'code': 1000, 'msg': 'Login successfully', 'data': result}
    else:
        return {'code': 1003, 'msg': 'Expired login information'}
