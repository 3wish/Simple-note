import { createApp } from 'vue'
import App from './App.vue'

// reset the default stylesheet
import "reset-css"

import router from "@/router"
import pinia from '@/store'

createApp(App)
.use(router)
.use(pinia)
.mount('#app')
