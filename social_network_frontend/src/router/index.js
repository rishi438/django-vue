import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import MessengerView from '../views/MessengerView.vue'
import SearchView from '../views/SearchView.vue'
import NotificationView from '../views/NotificationView.vue'
import ProfileView from '../views/ProfileView.vue'
import FriendsView from '../views/FriendsView.vue'
import PostView from '../views/PostDetailsView.vue'
import TrendView from '../views/TrendView.vue'
import EditProfileView from '../views/EditProfileView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/home',
            name: 'home',
            component: HomeView
        },
        {
            path: '/signup',
            name: 'signup',
            component: SignupView
        },
        {
            path: '/',
            name: 'login',
            component: LoginView
        },
        {
            path: '/chat',
            name: 'messenger',
            component: MessengerView
        },
        {
            path: '/search',
            name: 'search',
            component: SearchView
        },
        {
            path: '/notification',
            name: 'notification',
            component: NotificationView
        },
        {
            path: '/profile/:id',
            children: [
                {
                    path: '',
                    name: 'profile',
                    component: ProfileView
                },
                {
                    path: 'friends',
                    name: 'friends',
                    component: FriendsView
                },
                {
                    path: 'edit',
                    name: 'edit',
                    component: EditProfileView
                }
            ]
        },
        {
            path: '/post/:id',
            name: 'post_details',
            component: PostView
        },
        {
            path: '/trends/:id',
            name: 'trends',
            component: TrendView
        }
    ]
})

export default router
