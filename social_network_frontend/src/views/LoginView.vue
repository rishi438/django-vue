<template>
  <div class="md:h-screen h-full">
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 grid-cols-1 gap-4">
      <div class="main-left">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
          <div class="mb-6 text-2xl">Log In</div>
          <p class="mb-6 text-gray-500">
            Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
            Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
          </p>
          <p class="font-bold">
            doesn't have an account?
            <RouterLink :to="{ name: 'signup' }" class="underline"> Click here</RouterLink> to
            Signup!
          </p>
        </div>
      </div>
      <div class="main-right">
        <div class="p-12 bg-white border border-gray-200 rounded-lg">
          <form class="space-y-6" v-on:submit.prevent="submit_form">
            <div>
              <label>E-mail</label><br />
              <input type="email" placeholder="Your e-mail address" v-model="form.email"
                class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
            </div>
            <div>
              <label>Password</label><br />
              <input type="password" placeholder="Your password" v-model="form.password"
                class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
            </div>
            <template v-if="errors.length > 0">
              <div class="bg-red-300 text-white rounded-lg p-6">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
            </template>
            <div>
              <button class="py-3 px-6 bg-teal-500 hover:bg-teal-600 text-white rounded-lg">Log in</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '../stores/user'

export default {
  name: 'LoginView',
  setup() {
    let userStore = useUserStore()
    return {
      userStore
    }
  },
  mounted() {
    this.login_check()
  },
  data() {
    return {
      form: {
        email: '',
        password: ''
      },
      errors: []
    }
  },
  methods: {
    async submit_form() {
      this.errors = []
      if (this.form.email === '') {
        this.errors.push('Your e-mail is missing')
      }
      if (this.form.password === '') {
        this.errors.push('Your password is missing')
      }
      if (this.errors.length === 0) {
        await axios
          .post('/api/login/', this.form)
          .then((response) => {
            this.userStore.set_token(response.data)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
          })
          .catch((error) => {
            console.log('error ', error)
          })
        await axios
          .get('/api/me/')
          .then((response) => {
            this.userStore.set_user_info(response.data)
            this.$router.push('/home')
          })
          .catch((error) => {
            console.log('error ', error)
          })
      }
    },
    login_check() {
      if (this.userStore.user.is_authenticated) {
        this.$router.push('/home')
      }
    }
  }
}
</script>
