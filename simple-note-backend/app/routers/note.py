from fastapi import APIRouter
from pydantic import BaseModel

from ..schemas import note

router = APIRouter(
    prefix='/note',
    tags=['note']
)


class NoteInfo(BaseModel):
    title: str
    content: str


class NewNoteInfo(BaseModel):
    title: str | None = None
    content: str | None = None


@router.post('/new')
async def create_note(username: str, note_info: NoteInfo):
    try:
        result = note.add_note(username, **note_info.dict())
    except Exception as e:
        print(e)
        return {'code': 1101, 'msg': 'Failed to add'}
    else:
        return {'code': 1000, 'msg': 'Add successfully', 'noteList': result}


@router.post('/delete')
async def delete_note(note_id: str):
    result = note.delete_note(note_id)
    if result == 'ok':
        return {'code': 1000, 'msg': 'Delete successfully'}
    else:
        return {'code': 1102, 'msg': 'Failed to delete'}


@router.post('/update')
async def update_note(note_id: str, username: str, new_note_info: NewNoteInfo):
    try:
        result = note.update_note(note_id, username, **new_note_info.dict())
    except Exception as e:
        print("update with wrong:", e)
        return {'code': 1103, 'msg': 'Failed to Update'}
    else:
        return {'code': 1000, 'msg': 'Update successfully', 'noteList': result}


@router.get('/notes')
async def get_notes(username: str):
    notelist = note.get_user_note(username)
    return {'code': 1000, 'msg': f"{username}'s notes", 'noteList': notelist}
