import request from "./request";

const getNotes = username => {
  return request.get(
    `/note/notes?username=${username}`,
  );
}

const createNote = (username, data) => {
  return request.post(
    `/note/new?username=${username}`,
    data,
  )
}

const updateNote = (username, noteId, data) => {
  return request.post(
    `/note/update?note_id=${noteId}&username=${username}`,
    data,
  );
}

const deleteNote = noteId => {
  return request.post(
    `/note/delete?note_id=${noteId}`
  )
}

export { getNotes, createNote, updateNote, deleteNote}