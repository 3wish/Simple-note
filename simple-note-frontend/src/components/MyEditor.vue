<template>
  <div class="editor">
    <div class="title">
      Title: <input type="text" v-model="title">
    </div>
    <Toolbar style="border-bottom: 1px solid #ccc;" :editor="editorRef" :defaultConfig="toolbarConfig" :mode="mode" />
    <Editor style="height: 300px; overflow-y: hidden;" v-model="valueHtml" :defaultConfig="editorConfig" :mode="mode"
      @onCreated="handleCreated" />
    <div class="operation-btn">
      <button @click="saveNote">save</button>
      <button @click="deleteNote">delete</button>
    </div>
  </div>
</template>

<script setup>
import '@wangeditor/editor/dist/css/style.css' // 引入 css

import { onBeforeUnmount, ref, shallowRef, onMounted } from 'vue'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'

import useNotesStore from '@/store/notes';
import useUserStore from '@/store/user';

// 编辑器实例，必须用 shallowRef
const editorRef = shallowRef()

// 内容 HTML
const valueHtml = ref(props.content)

// 模拟 ajax 异步获取内容
// onMounted(() => {
//   setTimeout(() => {
//     // valueHtml.value = '<p>模拟 Ajax 异步设置内容</p>'
//     valueHtml.value = props.content;
//   }, 1500)
// })

const toolbarConfig = {}
const editorConfig = { placeholder: 'Please Write Your Note...' }

const notesStore = useNotesStore();
const userStore = useUserStore();
const props = defineProps(['title', 'content', 'noteId', 'noteIndex'])
const title = ref(props.title)

const saveNote = async () => {
  if (!title.value) {
    alert('Title cannot be null');
  } else {
    // update an existed note
    if (props.noteId != 'n') {
      const data = {};
      if (title.value != props.title) {
        data.title = title.value;
      }
      if (valueHtml.value != props.content) {
        data.content = valueHtml.value;
      }
      console.log(data);
      await notesStore.saveUpdatedNote(
        userStore.profile.username, 
        props.noteId, 
        data
      )
    // create a note
    } else {
      const data = {title: title.value, content: valueHtml.value}
      await notesStore.saveTempNote(userStore.profile.username, data);
    }
  }
}

const deleteNote = async () => {
  const isDeleted = confirm(`Are you sure to delete note:\n${title.value}?`);
  if (isDeleted) {
    notesStore.noteList.splice(props.noteIndex, 1);
    await notesStore.deleteExistedNote(props.noteId);
  }
}

// 组件销毁时，也及时销毁编辑器
onBeforeUnmount(() => {
  const editor = editorRef.value
  if (editor == null) return
  editor.destroy()
})

const handleCreated = (editor) => {
  editorRef.value = editor // 记录 editor 实例，重要！
}

</script>    

<style lang="scss" scoped>
.editor {
  margin-bottom: 10px;

  .title {
    color: white;
    margin-bottom: 5px;

    input {
      width: 30%;
      height: 20px;
    }
  }

  .operation-btn {
    width: 120px;
    margin: 0px auto;
    display: flex;
    justify-content: space-between;

    button {
      width: 50px;
      height: 30px;
    }
  }
}
</style>