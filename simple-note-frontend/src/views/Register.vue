<template>
  <div class="register-info">
    <div id="username" class="input-info">
      Username
      <input type="text" placeholder="At lease 5 characters" name="username" v-model="registerInfo.username">
    </div>
    <div id="password" class="input-info">
      Password
      <input type="password" placeholder="8 to 16 characters" name="password" v-model="registerInfo.password">
    </div>
    <div id="repeat-password" class="input-info">
      Confirm password
      <input type="password" placeholder="repeat the password" name="rePassword" v-model="registerInfo.rePassword">
    </div>
    <div class="register-btn">
      <button @click="register">Register</button>
    </div>
  </div>
</template>

<script setup>
import { userRegister } from '@/api/user';
import router from '@/router';
import { useRoute } from 'vue-router';

const route = useRoute();

const registerInfo = reactive({
  username: '',
  password: '',
  rePassword: '',
});

const register = async () => {
  if (!registerInfo.username || !registerInfo.password || !registerInfo.rePassword) {
    alert('Register information cannot be null');
  } else if (registerInfo.username.length < 5) {
    alert('username is too short');
  } else if (registerInfo.password.length < 8 || registerInfo.password.length > 16) {
    alert('The numbers of the password characters should be 8 to 16')
  } else if (registerInfo.password != registerInfo.rePassword) {
    alert('password is not the same');
  } else {
    let res = await userRegister(registerInfo.username, registerInfo.password);
    // console.log(res);
    if (res.code === 1000) {
      alert(res.msg);
      router.push('/login');
    } else {

    }
  }
}
</script>

<style lang="scss" scoped>
.register-info {
  width: 400px;
  height: 300px;
  margin: 200px auto 0 auto;

  .input-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;

    input {
      width: 200px;
      height: 25px;
    }
  }

  .register-btn {
    width: 100%;
    display: flex;
    justify-content: flex-end;

    button {
      background-color: #9eaaa5;
    }
  }

}
</style>