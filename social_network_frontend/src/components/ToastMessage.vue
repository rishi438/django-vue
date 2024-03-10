<template>
    <div
        v-if="store.is_visible"
        :class="[
            'text-white px-6 py-6 fixed rounded-xl ',
            'inset-x-0 max-w-max mx-auto toast-fall',
            store.status ? 'bg-emerald-500' : 'bg-red-500'
        ]"
    >
        {{ store.message }}
    </div>
</template>

<script setup>
import { useToastStore } from '@/stores/toast'

let store = useToastStore()
</script>
