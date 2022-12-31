import { defineStore } from "pinia";

import { userLogin, userAutoLogin } from "@/api/user";

export default defineStore('user', () => {
  const profile = ref({});
  const isLogin = ref(false);

  const getUser = async (formData, isKeep) => {
    let res = await userLogin(formData, isKeep);
    if (res.code === 1000) {
      if (isKeep) {
        let token = res.data.token.accessToken;
        let tokenType = res.data.token.tokenType;
        localStorage.setItem('noteToken', tokenType + ' ' + token);
      }
      profile.value = res.data.profile;
      isLogin.value = true;
    }
    return res.code
  }

  const autoLogin = async token => {
    let res = await userAutoLogin(token);
    if (res.code == 1000) {
      profile.value = res.data;
      isLogin.value = true;
    } else {
      localStorage.clear();
    }
  }

  const clearState = () => {
    profile.value = {};
    isLogin.value = false;
  }

  return { profile, isLogin, getUser, autoLogin, clearState }
})