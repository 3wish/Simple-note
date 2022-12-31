<template>
  <div>
    <div class="no-login" v-if="!isLogin">
      <h2>Welcome to My Note Site.</h2>
      <h2>Does not have a account yet? <strong>Register!</strong></h2>
      <h2>Already have a account? Login and Note!</h2>
    </div>
    <div class="logined" v-if="isLogin">
      <h2>Welcome back <em>{{ nickName ? nickName : username }}</em></h2>
      <h2>I know you have something to write. Let's go</h2>
      <u class="login-out" @click="loginOut">Login out</u>
    </div>
  </div>
</template>

<script setup>
import useUserStore from "@/store/user"
import useNotesStore from '@/store/notes'

const userStore = useUserStore();
const notesStore = useNotesStore();
const isLogin = ref(false);
isLogin.value = userStore.isLogin;
const username = userStore.profile.username;
const nickName = userStore.profile.nickName;

const loginOut = () => {
  localStorage.clear();
  userStore.clearState();
  notesStore.clearNoteList();
  isLogin.value = userStore.isLogin;
}
</script>

<style lang="scss" scoped>
.no-login,
.logined {
  width: 600px;
  margin: 0 auto;
  margin-top: 300px;
  font-size: 30px;

  h2 {
    line-height: 50px;
  }

  .login-out {
    &:hover {
      cursor: pointer;
    }
  }
}
</style>