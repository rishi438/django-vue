<template>
    <div class="max-w-7xl mx-auto grid grid-cols-12 gap-4">
        <div class="main-left md:col-span-3 col-span-12 order-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div class="text-center">
                    <img
                        src="/src/assets/1639256761455.jpeg"
                        class="profile-img lg:w-[150px] lg:h-[150px] md:h-[90px] md:w-[90px] mb-6 rounded-full mx-auto"
                    />
                    <p>
                        <strong>{{ user.name }}</strong>
                    </p>
                </div>
                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink
                        :to="{ name: 'friends', params: { id: user.id } }"
                        class="text-xs text-gray-500"
                        >{{ user.friends_count }}
                        {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                    </RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>
                <div class="flex flex-col">
                    <button
                        class="mt-6 flex-auto py-2 sm:px-6 px-4 bg-cyan-500 text-white rounded"
                        v-if="userStore.user.id != user.id"
                        @click="send_friend_request"
                    >
                        Add friend
                    </button>
                    <button
                        class="mt-3 flex-auto py-2 sm:px-6 px-4 bg-cyan-500 text-white rounded"
                        v-if="userStore.user.id != user.id"
                        @click="send_message"
                    >
                        Message
                    </button>
                </div>
            </div>
        </div>
        <div class="main-left md:col-span-9 space-y-2 col-span-12 sm:order-2 order-2">
            <div
                class="bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <form v-on:submit.prevent="submit_form" method="post">
                    <div class="p-4">
                        <textarea
                            v-model="body"
                            class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="What are you thinking about?"
                        ></textarea>
                    </div>
                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button
                            class="inline-block py-2 sm:px-6 px-4 bg-gray-600 hover:bg-gray-700 text-white rounded"
                        >
                            Attach image
                        </button>
                        <button
                            class="inline-block py-2 sm:px-6 px-4 bg-teal-500 text-white rounded"
                        >
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
import Trends from '../components/TrendsNetwork.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '../stores/user'
import { useToastStore } from '../stores/toast'

export default (await import('vue')).defineComponent({
    name: 'ProfileView',
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()
        return {
            userStore,
            toastStore
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
        send_friend_request() {
            axios
                .post(`/api/friends/${this.$route.params.id}/request/`)
                .then((response) => {
                    if (response.data.msg == 'Friend request already sent!') {
                        this.toastStore.showToast(5000, response.data.msg, 'bg-red-400')
                    } else {
                        this.toastStore.showToast(5000, response.data.msg, 'bg-green-500')
                    }
                })
                .catch((error) => {
                    console.error('Error Occured: ', error)
                })
        },
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
                        throw response.error
                    }
                    this.posts.unshift(response.data)
                    this.body = ''
                })
                .catch((error) => {
                    console.error('error occured', error)
                })
        },
        send_message() {
            axios
                .post(`/api/chat/${this.$route.params.id}/get-or-create/`)
                .then(() => {
                    this.$router.push('/chat')
                })
                .catch((error) => {
                    console.error(error)
                })
        }
    }
})
</script>
