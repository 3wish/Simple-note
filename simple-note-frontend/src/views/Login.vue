<template>
  <div class="register-info">
    <div id="username" class="input-info">
      Username
      <input type="text" name="username" v-model="registerInfo.username">
    </div>
    <div id="password" class="input-info">
      Password
      <input type="password" name="password" v-model="registerInfo.password">
    </div>
    <div class="register-btn">
      <div class="keep-login"><input type="checkbox" v-model="isKeep"> Keep login for 1 days</div>
      <button @click="login">Login</button>
    </div>
  </div>
</template>

<script setup>
import router from '@/router';
import useUserStore from '@/store/user'

const userStore = useUserStore();

const registerInfo = reactive({
  username: '',
  password: '',
});
const isKeep = ref(false);

const login = async () => {
  let formData = new FormData();
  formData.append('username', registerInfo.username)
  formData.append('password', registerInfo.password)

  let res =  await userStore.getUser(formData, isKeep.value);
  if (res == 1000) {
    router.push('/notes');
  } else {
    alert('Incorrect username or password');
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
    justify-content: space-between;
    align-items: center;

    .keep-login {
      font-size: 15px;

      input {
        margin: 0;
      }
    }

    button {
      background-color: #9eaaa5;
    }
  }

}
</style>