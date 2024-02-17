<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center md:col-span-3 col-span-4 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submit_form" class="p-6 flex space-x-4">
                    <input
                        v-model="query"
                        type="search"
                        class="p-3 w-full bg-gray-100 rounded-lg"
                        placeholder="What are you looking for?"
                    />
                    <button
                        class="inline-block py-2 px-6 bg-teal-500 hover:bg-teal-600 text-white rounded-lg self-center"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            class="w-6 h-6"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
                            ></path>
                        </svg>
                    </button>
                </form>
            </div>
            <div
                v-if="users.length"
                class="p-4 bg-white border border-gray-200 rounded-lg grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 lg:gap-5 md:gap-3 grid-cols-1 gap-2"
            >
                <div
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for="user in users"
                    v-bind:key="user.id"
                >
                    <div class="text-center">
                        <img
                            src="../assets/images/kung-fu-panda.jpeg"
                            class="mb-6 rounded-full w-[130px] h-[130px] mx-auto"
                        />
                        <p>
                            <strong>
                                <RouterLink :to="{ name: 'profile', params: { id: user.id } }">{{
                                    user.name
                                }}</RouterLink>
                            </strong>
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
                </div>
            </div>
            <div
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem :post="post" />
            </div>
        </div>
        <div class="main-right md:col-span-1 col-span-4 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import axios from 'axios';
import Trends from '../components/TrendsNetwork.vue';
import FeedItem from '../components/FeedItem.vue';
import { RouterLink } from 'vue-router';

export default (await import('vue')).defineComponent({
    name: 'SearchView',
    components: {
        PeopleYouMayKnow,
        Trends,
        RouterLink,
        FeedItem
    },
    data() {
        return {
            query: '',
            users: [],
            posts: []
        };
    },
    methods: {
        submit_form() {
            axios
                .post('/api/search/', {
                    query: this.query
                })
                .then((response) => {
                    this.users = response.data.users;
                    this.posts = response.data.posts;
                })
                .catch((error) => {
                    console.error('Error Occured: ', error);
                })
        }
    }
});
</script>
