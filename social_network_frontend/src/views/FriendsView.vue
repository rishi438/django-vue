<template>
    <div class="max-w-7xl mx-auto grid grid-cols-12 gap-2">
        <div class="main-left lg:col-span-3 md:col-span-3 col-span-12 order-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div class="text-center py-4">
                    <img
                        src="/src/assets/images/kung-fu-panda.jpeg"
                        class="profile-img lg:w-[150px] lg:h-[150px] md:h-[80px] md:w-[80px] mb-6 rounded-full mx-auto"
                    />
                    <p>
                        <strong>{{ user.name }}</strong>
                    </p>
                </div>
                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink
                        :to="{ name: 'friends', params: { id: user.id } }"
                        class="text-xs text-gray-500"
                    >
                        {{ user.friends_count }}
                        {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                    </RouterLink>
                    <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                </div>
            </div>
        </div>
        <div
            class="main-center lg:col-span-6 md:col-span-5 space-y-2 sm:col-span-7 col-span-12 sm:order-2 order-3"
        >
            <div
                v-if="friend_requests.length"
                class="p-4 bg-white border border-gray-200 rounded-lg gap-2"
            >
                <hr />
                <h2 class="text-xl mb-6">Friend Requests</h2>
                <div
                    class="p-4 text-center bg-gray-100 rounded-lg"
                    v-for="friend in friend_requests"
                    v-bind:key="friend.id"
                >
                    <div class="text-center">
                        <img
                            src="../assets/images/kung-fu-panda.jpeg"
                            class="mb-6 rounded-full w-[180px] h-[180px] mx-auto"
                        />
                        <p>
                            <strong>
                                <RouterLink
                                    :to="{ name: 'profile', params: { id: friend.created_by.id } }"
                                    >{{ friend.created_by.name }}</RouterLink
                                >
                            </strong>
                        </p>
                    </div>
                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">
                            {{ friend.friends_count }}
                            {{ friend.friends_count == 1 ? 'friend' : 'friends' }}
                        </p>
                        <p class="text-xs text-gray-500">{{ friend.posts_count }} posts</p>
                    </div>
                    <div class="mt-6">
                        <button
                            class="inline-block py-2 sm:px-6 px-4 bg-lime-600 text-white rounded mx-2"
                            @click="handler_request('ACCEPTED', friend.created_by.id)"
                        >
                            Accept
                        </button>
                        <button
                            class="inline-block py-2 sm:px-6 px-4 bg-red-700 text-white rounded mx-2"
                            @click="handler_request('REJECTED', friend.created_by.id)"
                        >
                            Reject
                        </button>
                    </div>
                </div>
            </div>
            <div
                v-if="friends.length"
                class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-2 gap-2"
            >
                <div
                    class="text-center bg-gray-100 rounded-lg py-5"
                    v-for="friend in friends"
                    v-bind:key="friend.id"
                >
                    <div class="text-center">
                        <img
                            src="../assets/images/kung-fu-panda.jpeg"
                            class="mb-6 rounded-full w-[150px] h-[150px] mx-auto"
                        />
                        <p>
                            <strong>
                                <RouterLink :to="{ name: 'profile', params: { id: friend.id } }">{{
                                    friend.name
                                }}</RouterLink>
                            </strong>
                        </p>
                    </div>
                    <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">
                            {{ user.friends_count }}
                            {{ user.friends_count == 1 ? 'friend' : 'friends' }}
                        </p>
                        <p class="text-xs text-gray-500">{{ user.posts_count }} posts</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="main-right lg:col-span-3 md:col-span-4 space-y-2 col-span-12 order-2">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import Trends from '../components/TrendsNetwork.vue';
import { useUserStore } from '../stores/user';
import { RouterLink } from 'vue-router';
import { useToastStore } from '../stores/toast';

export default (await import('vue')).defineComponent({
    name: 'FriendsView',
    setup() {
        const userStore = useUserStore();
        const toastStore = useToastStore();
        return {
            userStore,
            toastStore
        };
    },
    components: {
        PeopleYouMayKnow,
        Trends,
        RouterLink
    },
    data() {
        return {
            user: {},
            friend_requests: [],
            friends: []
        };
    },
    mounted() {
        this.get_friends();
    },
    methods: {
        get_friends() {
            axios
                .get(`/api/friends/${this.$route.params.id}/`)
                .then((response) => {
                    this.friend_requests = response.data.requests;
                    this.friends = response.data.friends;
                    this.user = response.data.user;
                })
                .catch((error) => {
                    console.log('error', error);
                })
        },
        handler_request(status, id) {
            axios
                .post(`/api/friends/${id}/${status}/`)
                .then((response) => {
                    console.log(response);
                    window.location.reload();
                })
                .catch((error) => {
                    console.error('Error Occured: ', error);
                })
        }
    }
});
</script>
