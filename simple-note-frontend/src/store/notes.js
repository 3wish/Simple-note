import { defineStore } from "pinia";
import { getNotes, createNote, deleteNote, updateNote } from "@/api/note";

export default defineStore('notes', () => {
  const noteList = ref([]);

  const tempNewNote = ref({
    noteId: 'n',
    title: '',
    content: ''
  });

  const getNoteList = async username => {
    let res = await getNotes(username);
    noteList.value = res.noteList;
  }

  const addTempNote = () => {
    noteList.value.push(tempNewNote);
  }

  const saveTempNote = async (username, data) => {
    let res = await createNote(username, data);
    if (res.code === 1000) {
      noteList.value = res.noteList;
    } else {
      alert(res.msg);
    }
  }

  const saveUpdatedNote = async (username, noteId, data) => {
    let res = await updateNote(username, noteId, data);
    if (res.code === 1000) {
      noteList.value = res.noteList;
      console.log(noteList.value);
    }
  }

  const deleteExistedNote = async (noteId, noteIndex) => {
    await deleteNote(noteId);
  }

  const clearNoteList = () => {
    noteList.value = [];
  }

  return { 
    noteList, 
    getNoteList, 
    addTempNote, 
    saveTempNote, 
    saveUpdatedNote,
    deleteExistedNote, 
    clearNoteList,
  }
});