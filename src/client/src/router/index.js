import { createRouter, createWebHistory } from 'vue-router';
import BasicPage from '@/components/layout/BasicPage.vue';
import Home from '@/pages/Home.vue';
import Login from '@/pages/Login.vue';

const routes = [
  {
    path: '/',
    component: BasicPage,
    children: [
      {
        path: '/home',
        component: Home,
      },
      {
        path: '/login',
        component: Login,
        meta: { unnecessaryAuth: true },
      },
    ],
  },
];

const router = createRouter({
  mode: 'history',
  history: createWebHistory(),
  routes,
});

export default router;
