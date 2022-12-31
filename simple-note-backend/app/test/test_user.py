from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        '/user/register',
        json={'username': 'test3', 'password': 123456}
    )
    assert response.status_code == 200
    assert response.json() == {'code': 1000, 'msg': 'Register successfully'}


def test_get_access_token():
    response = client.post(
        '/user/token',
        json='username=dasert&password=12345',
    )
    assert response.status_code == 200


def test_get_user():
    response = client.get(
        '/user/login',
        headers={'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MSIsImV4cCI6MTY2OTYzMzEyMH0.mJbyV3y6bcTFlGCgBii-oEJmfuS7ODqtbXGN6JSt-ns"}
    )
    print(response.json())
    assert response.status_code == 200