<template>
  <Menu as="div" class="relative inline-block text-left">
    <div>
      <MenuButton
        class="justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900s hover:bg-gray-50"
      >
        <img v-if="d_name['image']" :src="d_name['url']" class="w-[30px] h-[30px] rounded-full" />
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
        <div class="py-1">
          <MenuItem v-slot="{ active }" v-for="(option, index) in options" :key="index">
            <a
              v-if="typeof option == 'string'"
              :href="'/'"
              v-on:click="logout()"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm'
              ]"
              >{{ option }}</a
            >
            <RouterLink
              v-else
              :to="{ name: option['name'].toLowerCase(), params: { id: option['user'].user.id } }"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm'
              ]"
              >{{ option['name'] }}</RouterLink
            >
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { RouterLink } from 'vue-router'
const props = defineProps({
  removeToken: {
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
})
const logout = async () => {
  // let removing_token = true
  try {
    await props.removeToken?.()
  } catch (error) {
    console.error('error occured: ', error)
  }
}
</script>
