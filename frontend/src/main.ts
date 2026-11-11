// components
import Form from "./components/Form.vue"
import App from './App.vue'

// external packages
import axios from "axios"
import VueAxios from "vue-axios"
import { createRouter, createWebHistory } from "vue-router"
import { createApp } from 'vue'

// style sheets
import "./style.css"

const app = createApp(App)

const routes = [
    {path: '/form', name: 'Form', component: Form}
]


const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

app.use(router)
app.use(VueAxios, axios)
app.mount("#app")