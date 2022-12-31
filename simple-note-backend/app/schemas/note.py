from collections.abc import Sequence

from ..crud import note
from ..database.models import Note


def add_note(username: str, title: str, content: str) -> list[dict[str, str] | None]:
    try:
        note.add_note(username, title, content)
    except Exception as e:
        raise e
    else:
        return get_user_note(username)


def delete_note(note_id: str):
    note_id: int = int(note_id[1:])
    try:
        note.delete_note(note_id)
    except Exception as e:
        print(e)
        return 'error'
    else:
        return 'ok'


def update_note(
        note_id: str,
        username: str,
        title: str | None = None,
        content: str | None = None,
):
    try:
        note.update_note(note_id, title, content)
    except Exception as e:
        raise e
    else:
        return get_user_note(username)


def get_user_note(username: str) -> list[dict[str, str] | None]:
    result: Sequence[Note] = note.get_user_note(username)
    notelist: list[dict[str, str]] = []
    for row in result:
        _note = {
            'noteId': 'n' + str(row.id),
            'title': row.title,
            'content': row.content,
            'createdAt': row.created_at,
            'updatedAt': row.updated_at,
        }
        notelist.append(_note)
    return notelist
