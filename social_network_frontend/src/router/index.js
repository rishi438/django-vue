import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import Signup from '../views/SignupView.vue'
import Login from '../views/LoginView.vue'
import Messenger from '../views/MessengerView.vue'
import Search from '../views/SearchView.vue'
import Notification from '../views/NotificationView.vue'
import Profile from '../views/ProfileView.vue'
import Friends from '../views/FriendsView.vue'
import PostView from '../views/PostDetailsView.vue'

const router = createRouter({
  // @ts-ignore
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/messenger',
      name: 'messenger',
      component: Messenger
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/notification',
      name: 'notification',
      component: Notification
    },
    {
      path: '/profile/:id',
      children: [
        {
          path: '',
          name: 'profile',
          component: Profile
        },
        {
          path: 'friends',
          name: 'friends',
          component: Friends
        }
      ]
    },
    {
      path: '/post/:id',
      name: 'post_details',
      component: PostView
    }
  ]
})

export default router
