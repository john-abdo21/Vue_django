import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import store from '@/store';
import router from '@/router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faCircleUser,
  faUserPen,
  faRightFromBracket,
} from '@fortawesome/free-solid-svg-icons';

library.add(faCircleUser, faUserPen, faRightFromBracket);

createApp(App)
  .component('FAI', FontAwesomeIcon)
  .use(store)
  .use(router)
  .mount('#app');
