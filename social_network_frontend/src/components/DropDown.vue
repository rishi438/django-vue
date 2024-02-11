<template>
    <Menu as="div" class="relative inline-block text-left">
        <div>
            <MenuButton
                class="justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900s hover:bg-stone-200"
            >
                <img
                    v-if="d_name['image']"
                    :src="d_name['url']"
                    class="w-[30px] h-[30px] rounded-full"
                />
                <span v-else>{{ d_name }}</span>
            </MenuButton>
        </div>

        <transition
            enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95"
        >
            <MenuItems
                class="absolute right-0 z-10 mt-2 w-56 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
            >
                <div>
                    <MenuItem v-slot="{ active }" v-for="(option, index) in options" :key="index">
                        <div
                            v-if="typeof option == 'string'"
                            v-on:click="logout"
                            :class="[
                                active ? 'bg-teal-200 text-gray-900' : 'text-gray-700',
                                'block px-4 py-2 text-sm rounded-md cursor-pointer'
                            ]"
                        >
                            {{ option }}
                        </div>
                        <RouterLink
                            v-else-if="option['name'] != 'Profile'"
                            :to="{
                                name: option['name'].toLowerCase(),
                                params: { id: option['val'].user.id }
                            }"
                            :class="[
                                active ? 'bg-teal-200 text-gray-900' : 'text-gray-700',
                                'block px-4 py-2 text-sm rounded-md'
                            ]"
                            @click="$emit('close')"
                        >
                            {{ option['name'] }}
                        </RouterLink>
                        <RouterLink
                            v-else
                            :to="{
                                name: 'profile',
                                params: { id: option['val'].user.id }
                            }"
                            :class="[
                                active ? 'bg-teal-200 text-gray-900' : 'text-gray-700',
                                'block px-4 py-2 text-sm rounded-md'
                            ]"
                            @click="$emit('close')"
                        >
                            {{ option['name'] }}
                        </RouterLink>
                    </MenuItem>
                </div>
            </MenuItems>
        </transition>
    </Menu>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { RouterLink, useRouter } from 'vue-router';

const router = useRouter()
const props = defineProps({
    remove_token: {
        type: Function
    },
    d_name: {
        type: Object,
        required: true
    },
    options: {
        type: Array,
        required: true
    }
});
const logout = async () => {
    try {
        await props.remove_token?.();
        router.push('/');
    } catch (error) {
        console.error('error occured: ', error);
    }
};
</script>
