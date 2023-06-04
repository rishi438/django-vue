import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import signupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import MessengerView from '../views/MessengerView.vue'
import SearchView from '../views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: signupView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/messenger',
      name: 'messenger',
      component: MessengerView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    }
  ]
})

export default router
