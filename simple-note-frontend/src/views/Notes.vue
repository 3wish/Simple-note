<template>
  <div class="note-panel">
    <h2 class="headline">
      Here is your note,
      <u>{{ nickName ? nickName : username }}</u>,
      <u class="login-out" @click="loginOut">Login out</u>
    </h2>
    <ul class="notelist">
      <ul class="note" v-for="(note, index) in noteList" :key="note.noteId">
        <ul class="title-bar">
          <ul class="title" @click="triggerNote(index)">
            <h3 class="note-title">{{ note.title }}</h3>
            <ul class="time">
              <li>
                <span v-if="note.createdAt">created at:</span>
                {{ note.createdAt }}
              </li>
              <li>
                <span v-if="note.updatedAt">updated at:</span>
                {{ note.updatedAt }}
              </li>
            </ul>
          </ul>
        </ul>
        <MyEditor 
         :title="note.title" 
         :content="note.content" 
         :noteId="note.noteId"
         :noteIndex="index"
         v-if="isOpened[index]">
        </MyEditor>
      </ul>
    </ul>
    <button id="new" @click="addTempNote">new</button>
  </div>
</template>

<script setup>
import MyEditor from '@/components/MyEditor.vue'

import useUserStore from '@/store/user';
import useNotesStore from '@/store/notes';
import router from '@/router';


const userStore = useUserStore();
const username = userStore.profile.username;
const nickName = userStore.profile.nickName;

const notesStore = useNotesStore();

const loginOut = () => {
  localStorage.clear();
  userStore.clearState();
  notesStore.clearNoteList();
  router.push('/');
}

const noteList = ref(notesStore.noteList)
const isOpened = ref(new Array(noteList.value.length).fill(false));

const triggerNote = index => {
  isOpened.value[index] = !isOpened.value[index]
}

const addTempNote = () => {
  // notesStore.addTempNote();
  isOpened.value.push(true);
  noteList.value.push({noteId: 'n', title: '', content: ''})
}

watch(
  () => notesStore.noteList,
  (newValue) => {
    console.log("111:", newValue);
    noteList.value = newValue;
    isOpened.value = new Array(noteList.value.length).fill(false)
  }
)

</script>

<style lang="scss" scoped>
.note-panel {
  margin: 50px auto 0px auto;
  width: 50%;

  .headline {
    font-size: 25px;
    margin-bottom: 50px;
    text-align: center;

    .login-out {
      cursor: pointer;
    }
  }

  #new {
    width: 50px;
    height: 30px;
    font-size: 14px;
    display: block;
    margin: auto;
  }



  .notelist {
    background-color: #424a53;
    padding: 10px;
    border-radius: 5px;

    .title-bar {
      font-size: 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;

      .title {
        width: 100%;
        border: 1px solid;
        border-radius: 5px;
        background-color: rgb(225, 224, 224);
        cursor: pointer;

        .time {
          font-size: 14px;
          color: gray;
        }
      }

      .operation {
        display: flex;
        justify-content: space-between;
        width: 12%;
        color: white;

        li {
          width: 55px;
          line-height: 40px;
          text-align: center;
          border-radius: 5px;
          border: 1px solid;
          cursor: pointer;
        }
      }
    }
  }
}
</style>

