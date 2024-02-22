// eslint-disable-next-line no-unused-vars
import { defineStore } from 'pinia'
import axios from 'axios'

// eslint-disable-next-line no-undef
export let useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            is_authenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,
            avatar_url: null
        }
    }),

    actions: {
        init_store() {
            if (localStorage.getItem('user.access')) {
                this.user.access = localStorage.getItem('user.access')
                this.user.refresh = localStorage.getItem('user.refresh')
                this.user.id = localStorage.getItem('user.id')
                this.user.name = localStorage.getItem('user.name')
                this.user.email = localStorage.getItem('user.email')
                this.user.friends_count = localStorage.getItem('user.friends_count')
                this.user.posts_count = localStorage.getItem('user.posts_count')
                this.user.avatar_url = localStorage.getItem('user.avatar_url')
                this.user.is_authenticated = true
                this.refresh_token()
            }
        },

        set_token(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.is_authenticated = true
            localStorage.setItem('user.access', data.access)
            localStorage.setItem('user.refresh', data.refresh)
        },

        set_attribute(data, initial_store = false) {
            for (const key in data) {
                if (!initial_store) {
                    const value = this.user[key]
                    if (!isNaN(value)) {
                        this.user[key] = parseInt(value) + parseInt(data[key])
                    } else {
                        this.user[key] = data[key]
                    }
                } else {
                    this.user[key] = data[key]
                }
                localStorage.setItem(`user.${key}`, this.user[key])
            }
        },

        remove_token() {
            this.user.is_authenticated = false
            this.user.refresh = null
            this.user.access = null
            this.user.id = false
            this.user.name = false
            this.user.email = false
            this.user.friends_count = false
            this.user.posts_count = false
            this.user.avatar_url = null

            localStorage.setItem('user.is_authenticated', '')
            localStorage.setItem('user.access', '')
            localStorage.setItem('user.refresh', '')
            localStorage.setItem('user.id', '')
            localStorage.setItem('user.name', '')
            localStorage.setItem('user.email', '')
            localStorage.setItem('user.friends_count', '')
            localStorage.setItem('user.posts_count', '')
            localStorage.setItem('user.avatar_url', '')
        },

        refresh_token() {
            axios
                .post('/api/refresh/', {
                    refresh: this.user.refresh
                })
                .then((response) => {
                    this.user.access = response.data.access
                    localStorage.setItem('user.access', response.data.access)
                    axios.defaults.headers.common[
                        'Authorization'
                    ] = `Bearer ${response.data.access}`
                })
                .catch((error) => {
                    this.remove_token()
                    console.log(error)
                })
        },

        set_image() {
            return this.user.avatar_url
                ? this.user.avatar_url
                : '/src/assets/images/kung-fu-panda.jpeg'
        }
    }
})
