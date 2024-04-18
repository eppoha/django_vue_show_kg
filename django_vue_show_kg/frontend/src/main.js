import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
axios.defaults.baseURL = 'http://localhost:8000';

createApp(App).use(router).use(ElementPlus).mount('#app')