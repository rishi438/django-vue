<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4" v-if="conversations.length">
        <div class="main-left md:col-span-1 col-span-4">
            <div class="bg-white border border-gray-200 text-center rounded-lg">
                <ul class="space-y-4 overflow-hidden overflow-y-auto max-h-[75vh]" role="list">
                    <li
                        class="p-4 group/item flex items-center justify-between hover:bg-teal-200 hover:ring-teal-200 rounded-lg"
                        v-for="conversation in conversations"
                        :key="conversation.id"
                        v-on:click="set_active_conversation(conversation.id)"
                    >
                        <div class="flex items-center space-x-2">
                            <template v-for="user in conversation.users" :key="user.id">
                                <div v-if="userStore.user.id != user.id" class="flex items-center text-left">
                                    <img
                                        :src="user.avatar_url ? user.avatar_url : kungFuPandaImage"
                                        class="w-[40px] h-[40px] rounded-full"
                                    />
                                    <div class="text-sm font-medium ml-2">
                                        {{ user.name }}
                                    </div>
                                </div>
                            </template>
                        </div>
                        <span class="text-xs text-gray-500">{{
                            conversation.modified_at_formatted
                        }}</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="main-center md:col-span-3 md:block hidden col-span-4 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg overflow-hidden overflow-y-auto max-h-[53vh]">
                <div class="flex flex-col flex-grow p-4" v-if="active_conversation.messages?.length">
                    <template v-for="message in active_conversation.messages" :key="message.id">
                        <div
                            class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.created_by.id === userStore.user.id"
                        >
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">
                                        {{ message.body }}
                                    </p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none"
                                    >{{ message.created_at_formatted }} ago</span
                                >
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img
                                    :src="
                                        userStore.user.avatar_url ? userStore.user.avatar_url : kungFuPandaImage
                                    "
                                    class="w-[40px] h-[40px] rounded-full"
                                />
                            </div>
                        </div>
                        <div class="flex w-full mt-2 space-x-3 max-w-md" v-else>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img
                                    :src="
                                        message.avatar_url ? message.avatar_url : kungFuPandaImage
                                    "
                                    class="w-[40px] h-[40px] rounded-full"
                                />
                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm">
                                        {{ message.body }}
                                    </p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none"
                                    >{{ message.created_at_formatted }} ago</span
                                >
                            </div>
                        </div>
                    </template>
                </div>
            </div>
            <div class="bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submit_form">
                    <div class="p-4">
                        <textarea
                            v-model="body"
                            class="p-4 w-full bg-gray-100 rounded-lg resize-none"
                            placeholder="What do you want to say?"
                        ></textarea>
                    </div>
                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button class="inline-block py-2 px-6 bg-teal-500 text-white rounded-lg">
                            Send
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div v-else class="text-4xl flex h-[calc(100vh-128px)] justify-center items-center">
        Add friends to start conversation
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import kungFuPandaImage from '@/assets/images/kung-fu-panda.jpeg'

export default (await import('vue')).defineComponent({
    name: 'MessengerView',
    setup() {
        const userStore = useUserStore();
        return {
            userStore,
        }
    },
    data() {
        const prev_id = this.$router.options.history.state.back.split("/").pop();
        return {
            prev_id,
            conversations: [
                {
                    users: []
                }
            ],
            active_conversation: {},
            body: '',
            kungFuPandaImage
        }
    },
    mounted() {
        this.get_conversations()
    },
    methods: {
        get_conversations() {
            axios
                .get('/api/chat/')
                .then((response) => {
                    this.conversations = response.data
                    if (this.conversations.length) {
                        let check = this.conversations.filter(chat => chat.users.some(user => user.id === this.prev_id))
                        this.active_conversation = check.length?check[0].id:this.conversations[0].id
                    }
                    this.get_messages()
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        get_messages() {
            axios
                .get(`/api/chat/${this.active_conversation}/`)
                .then((response) => {
                    this.active_conversation = response.data
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        submit_form() {
            axios
                .post(`/api/chat/${this.active_conversation.id}/send/`, {
                    body: this.body
                })
                .then((response) => {
                    this.active_conversation.messages.push(response.data)
                    this.body = ''
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        set_active_conversation(id) {
            if(id){
                this.active_conversation = id
                this.get_messages()
            }
        }
    }
})
</script>
