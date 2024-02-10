<template>
  <div class="max-w-8xl mx-auto grid grid-cols-12 gap-lg-4 gap-2">
    <div class="main-left md:col-span-8 space-y-2 sm:col-span-7 col-span-12 sm:order-2 order-3">
      <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h2 class="text-xl ">Trending: <span class="text-blue-600">#{{$route.params.id}}</span></h2>
      </div>
      <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" v-bind:key="post.id">
        <FeedItem :post="post" />
      </div>
    </div>
    <div class="main-right md:col-span-4 space-y-2 sm:col-span-5 col-span-12 sm:order-3 order-2">
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

export default (await import('vue')).defineComponent({
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
  watch: {
    '$route.params.id': {
      handler() {
        this.get_trend_feed()
      },
      deep: true,
      immediate: true
    }
  },
  data() {
    return {
      posts: [],
      body: ''
    }
  },
  methods: {
    get_trend_feed() {
      axios
        .get(`/api/post/?trend=${this.$route.params.id}`)
        .then((response) => {
          this.posts = response.data
        })
        .catch((error) => {
          console.log('error', error)
        })
    },
  }
});
</script>
