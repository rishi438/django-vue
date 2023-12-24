<template>
  <div class="max-w-7xl mx-auto grid grid-cols-12 gap-4">
    <div class="main-left md:col-span-3 col-span-12 order-1">
      <div class="main-left md:col-span-1 col-span-4">
        <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
          <div class="text-center">
            <img
              src="/src/assets/1639256761455.jpeg"
              class="profile-img w-[100px] h-[100px] mb-6 rounded-full mx-auto"
            />
            <p>
              <strong>{{ user.name }}</strong>
            </p>
          </div>
          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
    </div>
    <div class="main-left md:col-span-9 space-y-2 sm:col-span-7 col-span-12 sm:order-2 order-2">
      <div class="bg-white border border-gray-200 rounded-lg" v-if="userStore.user.id === user.id">
        <form v-on:submit.prevent="submit_form" method="post">
          <div class="p-4">
            <textarea
              v-model="body"
              class="p-4 w-full bg-gray-100 rounded-lg"
              placeholder="What are you thinking about?"
            ></textarea>
          </div>
          <div class="p-4 border-t border-gray-100 flex justify-between">
            <button class="inline-block py-2 sm:px-6 px-4 bg-gray-600 text-white rounded">
              Attach image
            </button>
            <button class="inline-block py-2 sm:px-6 px-4 bg-teal-500 text-white rounded">
              Post
            </button>
          </div>
        </form>
      </div>
      <div
        class="p-4 bg-white border border-gray-200 rounded-lg"
        v-for="post in posts"
        v-bind:key="post.id"
      >
        <FeedItem :post="post" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
// @ts-ignore
import Trends from '../components/TrendsNetwork.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user'

export default {
  name: 'Home',
  setup() {
    const userStore = useUserStore()
    return {
      userStore
    }
  },
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem
  },
  data() {
    return {
      posts: [],
      user: {},
      body: ''
    }
  },
  watch: {
    '$route.params.id': {
      handler() {
        this.get_feed()
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    get_feed() {
      axios
        .get(`/api/post/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.posts = response.data.post
          this.user = response.data.user
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
    submit_form() {
      axios
        .post('/api/post/create/', {
          body: this.body
        })
        .then((response) => {
          if (response.error) {
            throw error
          }
          this.posts.unshift(response.data)
          this.body = ''
        })
        .catch((error) => {
          console.error('error occured', error)
        })
    }
  }
}
</script>
