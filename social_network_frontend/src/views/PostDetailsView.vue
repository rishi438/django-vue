<template>
    <div class="max-w-8xl mx-auto grid grid-cols-12 gap-lg-4 gap-2">
        <div class="main-center lg:col-span-9 md:col-span-8 space-y-2 sm:col-span-7 col-span-12">
            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-if="post.id">
                <FeedItem :post="post" />
            </div>
            <div
                class="p-4 ml-6 bg-white border border-gray-200 rounded-lg"
                v-for="comment in post.comments"
                v-bind:key="comment.id"
            >
                <CommentItem :comment="comment" />
            </div>
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submit_form" method="post">
                    <div class="p-4">
                        <textarea
                            v-model="body"
                            class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="What do you think?"
                        ></textarea>
                    </div>
                    <div class="p-4 border-t border-gray-100">
                        <button
                            class="inline-block py-2 sm:px-6 px-4 bg-teal-500 text-white rounded"
                        >
                            Comment
                        </button>
                    </div>
                </form>
            </div>
        </div>
        <div class="main-right lg:col-span-3 md:col-span-4 space-y-2 sm:col-span-5 col-span-12">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/TrendsNetwork.vue'
import FeedItem from '../components/FeedItem.vue'
import CommentItem from '../components/CommentItem.vue'

export default (await import('vue')).defineComponent({
    name: 'PostView',
    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem,
        CommentItem
    },
    mounted() {
        this.get_post()
    },
    data() {
        return {
            post: {
                id: null,
                comments: {}
            },
            body: ''
        }
    },
    methods: {
        get_post() {
            axios
                .get(`/api/post/${this.$route.params.id}/`)
                .then((response) => {
                    this.post = response.data.post
                })
                .catch((error) => {
                    console.log('error', error)
                })
        },
        submit_form() {
            axios
                .post(`/api/post/${this.$route.params.id}/comment/`, {
                    body: this.body
                })
                .then((response) => {
                    if (response.error) {
                        throw response.error
                    }
                    this.post.comments.push(response.data)
                    this.body = ''
                })
                .catch((error) => {
                    console.error('error occured', error)
                })
        }
    }
})
</script>
