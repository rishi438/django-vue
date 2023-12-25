// eslint-disable-next-line no-unused-vars
import { defineStore } from 'pinia'
import axios from 'axios'
// eslint-disable-next-line no-undef
export let useUserStore = defineStore({
  id: 'user',

  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      name: null,
      email: null,
      access: null,
      refresh: null
    }
  }),
  actions: {
    initStore() {
      if (localStorage.getItem('user.access')) {
        this.user.access = localStorage.getItem('user.access')
        this.user.refresh = localStorage.getItem('user.refresh')
        this.user.id = localStorage.getItem('user.id')
        this.user.name = localStorage.getItem('user.name')
        this.user.email = localStorage.getItem('user.email')
        this.user.friends_count = localStorage.getItem('user.friends_count')
        this.user.isAuthenticated = true
        this.refreshToken()
      }
    },

    setToken(data) {
      this.user.access = data.access
      this.user.refresh = data.refresh
      this.user.isAuthenticated = true
      localStorage.setItem('user.access', data.access)
      localStorage.setItem('user.refresh', data.refresh)
    },

    removeToken() {
      console.log('removeToken')

      this.user.refresh = null
      this.user.access = null
      this.user.id = false
      this.user.name = false
      this.user.id = false
      this.user.email = false
      this.user.friends_count = false

      localStorage.setItem('user.access', '')
      localStorage.setItem('user.refresh', '')
      localStorage.setItem('user.id', '')
      localStorage.setItem('user.name', '')
      localStorage.setItem('user.email', '')
      localStorage.setItem('user.friends_count', '')
    },

    setUserInfo(user) {
      this.user.id = user.id
      this.user.name = user.name
      this.user.email = user.email
      this.user.friends_count = user.friends_count
      localStorage.setItem('user.id', this.user.id)
      localStorage.setItem('user.name', this.user.name)
      localStorage.setItem('user.email', this.user.email)
      localStorage.setItem('user.friends_count', this.user.friends_count)
    },

    refreshToken() {
      axios
        .post('/api/refresh/', {
          refresh: this.user.refresh
        })
        .then((response) => {
          this.user.access = response.data.access
          localStorage.setItem('user.access', response.data.access)
          axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`
        })
        .catch((error) => {
          console.log(error)
          this.removeToken()
        })
    }
  }
})
