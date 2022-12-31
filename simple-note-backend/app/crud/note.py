from collections.abc import Sequence

from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import Session

from app.database.db import engine
from app.database.models import Note, User
from . import user


def add_note(username: str, title: str, content: str):
    _user = user.get_user(username)
    with Session(engine) as session:
        try:
            session.execute(
                insert(Note),
                [
                    {
                        'title': title,
                        'content': content,
                        'author': _user,
                        'author_id': _user.id,
                    }
                ]
            )
        except Exception as e:
            raise e

        session.commit()


def delete_note(note_id: int):
    with Session(engine) as session:
        session.execute(
            delete(Note).where(Note.id == note_id)
        )
        session.commit()


def update_note(
        note_id: str,
        title: str | None = None,
        content: str | None = None
):
    note_id = int(note_id[1:])
    with Session(engine) as session:
        try:
            if content is not None:
                session.execute(
                    update(Note)
                    .where(Note.id == note_id)
                    .values(content=content)
                )
            if title is not None:
                session.execute(
                    update(Note)
                    .where(Note.id == note_id)
                    .values(title=title)
                )
        except Exception as e:
            raise e
        finally:
            session.commit()


def get_user_note(username: str) -> Sequence[Note]:
    with Session(engine) as session:
        stmt = select(Note).where(Note.author.has(User.username == username))
        result = session.scalars(stmt).all()
        return result
