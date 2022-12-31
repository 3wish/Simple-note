from fastapi import Depends
from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import Session

from app.database.models import User
from app.database.db import engine
from app.dependcies import get_session


def add_user(username: str, password: str):
    with Session(engine) as session:
        session.execute(insert(User).values([{'username': username, 'password': password}]))
        session.commit()


def get_user(username: str):
    with Session(engine) as session:
        result = session.scalars(select(User)
                        .where(User.username == username))\
                        .all()
        if result:
            print(result)
            return result[0]
        else:
            return False
