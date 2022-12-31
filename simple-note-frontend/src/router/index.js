import { createRouter, createWebHistory, useRouter } from 'vue-router';

import Home from '@/views/Home.vue';
import useUserStore from '@/store/user';
import useNotesStore from '@/store/notes';



const routes = [
  {
    path: '/',
    component: Home,
    name: 'Home',
    beforeEnter: async (to, from, next) => {
      const userStore = useUserStore();
      const notesStore = useNotesStore();
      const token = localStorage.getItem('noteToken');
      if (!userStore.isLogin && token) {
        await userStore.autoLogin(token);
        await notesStore.getNoteList(userStore.profile.username);
      }
      next()
    }
  },

  {
    path: '/home',
    redirect: '/',
  },

  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    beforeEnter: (to, from, next) => {
      const userStore = useUserStore();
      const isLogin = userStore.isLogin;
      if (isLogin) {
        alert('You have already logined!');
      } else {
        next();
      }
    }
  },

  {
    path: '/register',
    component: () => import('@/views/Register.vue'),
  },

  {
    path: '/notes',
    name: 'Note',
    component: () => import('@/views/Notes.vue'),
    beforeEnter: async (to, from, next) => {
      const userStore = useUserStore();
      const notesStore = useNotesStore();
      const token = localStorage.getItem('noteToken');
      if (!userStore.isLogin && token) {
        await userStore.autoLogin(token);
        const username = userStore.profile.username;
        await notesStore.getNoteList(username);
      }
      if (userStore.isLogin) {
        if (from.name === 'Login') {
          await notesStore.getNoteList(userStore.profile.username);
        }
        next();
      } else {
        alert("Please Login!")
        next({name: 'Home'})
      }
    },
  },

]

export default createRouter({
  history: createWebHistory(),
  routes
})