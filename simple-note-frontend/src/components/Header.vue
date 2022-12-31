<template>
  <div>
    <nav class="nav-bar">
      <h1>FastAPI + Vue + Vite</h1>
      <ul class="left-bar">
        <ul @click="goHome">
          <li :class="{ active: isActives[0] }">Home</li>
          <li id="triangle" v-if="isActives[0]"></li>
        </ul>
        <ul @click="goNotes">
          <li :class="{ active: isActives[1] }">Notes</li>
          <li id="triangle" v-if="isActives[1]"></li>
        </ul>
      </ul>
      <ul class="right-bar">
        <ul @click="goRegister">
          <li :class="{ active: isActives[2] }">Register</li>
          <li id="triangle" v-if="isActives[2]"></li>
        </ul>
        <ul @click="goLogin">
          <li :class="{ active: isActives[3] }">Login</li>
          <li id="triangle" v-if="isActives[3]"></li>
        </ul>
      </ul>
    </nav>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const pathToNumObj = {
  home: 0,
  notes: 1,
  register: 2,
  login: 3
}
const router = useRouter();
const route = useRoute();
const isActives = reactive([true, false, false, false]);

const changeStatus = n => {
  isActives.forEach((element, index) => {
    isActives[index] = false;
  });
  isActives[n] = !isActives[n];
}

watch(() => route.path, (newPath, oldPath) => {
  let pathName = newPath.slice(1);
  if (!pathName || pathName == 'home') {
    changeStatus(0);
  } else {
    changeStatus(pathToNumObj[pathName]);
  }
});

const goHome = () => {
  // changeStatus(0);
  router.push('/home');
}
const goNotes = () => {
  // changeStatus(1);
  router.push('/notes');
}

const goRegister = () => {
  // changeStatus(2);
  router.push('/register')
}

const goLogin = () => {
  // changeStatus(3);
  router.push('/login')
}
</script>

<style lang="scss" scoped>
.nav-bar {
  height: 55px;
  background-color: #212529;
  display: flex;
  padding: 0 10%;
  align-items: center;
  justify-content: space-between;

  h1 {
    color: white;
    font-size: 24px;
  }

  .left-bar,
  .right-bar {
    font-size: 18px;
    color: #b1aca5;
    display: flex;
    width: 200px;
    justify-content: space-between;

    ul {
      display: flex;
      flex-direction: column;
      align-items: center;

      &:hover {
        cursor: pointer;
      }

      .active {
        color: white;
      }
    }
  }

}

#triangle {
  position: absolute;
  top: 36px;
  width: 0px;
  height: 0px;
  border-top: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid white;
  border-left: 10px solid transparent;
}
</style>