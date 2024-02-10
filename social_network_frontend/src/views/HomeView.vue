<template>
  <div class="max-w-8xl mx-auto grid grid-cols-12 gap-lg-4 gap-2">
    <div class="main-left lg:col-span-3 md:col-span-3 col-span-12 order-1">
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        <div class="text-center py-4">
          <img src="/src/assets/1639256761455.jpeg"
            class="profile-img lg:w-[150px] lg:h-[150px] md:h-[80px] md:w-[80px] mb-6 rounded-full mx-auto" />
          <p>
            <strong>{{ userStore.user.name }}</strong>
          </p>
        </div>
        <div class="mt-6 flex space-x-8 justify-around">
          <RouterLink :to="{ name: 'friends', params: { id: userStore.user.id } }" class="text-xs text-gray-500">
            {{ userStore.user.friends_count }}
            {{ userStore.user.friends_count == 1 ? 'friend' : 'friends' }}
          </RouterLink>
          <p class="text-xs text-gray-500">{{ userStore.user.posts_count }} posts</p>
        </div>
      </div>
    </div>
    <div class="main-left lg:col-span-6 md:col-span-5 space-y-2 sm:col-span-7 col-span-12 sm:order-2 order-3">
      <div class="bg-white border border-gray-200 rounded-lg">
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
      <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
        <FeedItem :post="post" />
      </div>
    </div>
    <div class="main-right lg:col-span-3 md:col-span-4 space-y-2 sm:col-span-5 col-span-12 sm:order-3 order-2">
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/TrendsNetwork.vue'
import { useUserStore } from '../stores/user'
import FeedItem from '../components/FeedItem.vue'

export default {
  name: 'HomeView',
  components: {
    PeopleYouMayKnow,
    Trends,
    FeedItem
  },
  setup() {
    const userStore = useUserStore()
    return {
      userStore
    }
  },
  mounted() {
    this.get_feed()
  },
  data() {
    return {
      posts: [],
      body: ''
    }
  },
  methods: {
    get_feed() {
      axios
        .get('/api/post/')
        .then((response) => {
          this.posts = response.data
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
            throw response.error
          }
          this.posts.unshift(response.data)
          this.userStore.set_attribute({ "posts_count": 1 })
          this.body = ''
        })
        .catch((error) => {
          console.error('error occured', error)
        })
    }
  }
}
</script>
