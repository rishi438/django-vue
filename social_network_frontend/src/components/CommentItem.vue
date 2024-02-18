<template>
    <div class="mb-6 flex justify-between">
        <div class="flex items-center space-x-6">
            <img
                :src="
                    comment.created_by.avatar_url ? comment.created_by.avatar_url : kungFuPandaImage
                "
                class="w-[40px] h-[40px] rounded-full"
            />
            <div class="text-sm font-medium">
                <RouterLink
                    :to="{
                        name: 'profile',
                        params: { id: comment.created_by.id }
                    }"
                >
                    {{ comment.created_by.name }}
                </RouterLink>
            </div>
        </div>
        <div class="z-0 flex items-end">
            <p class="text-xs text-gray-600 mb-[-5px]">
                <span>{{ comment.created_at_formatted }} ago</span>
            </p>
        </div>
    </div>
    <p>{{ comment.body }}</p>
</template>

<script>
import { RouterLink } from 'vue-router'
import kungFuPandaImage from '@/assets/images/kung-fu-panda.jpeg'

export default (await import('vue')).defineComponent({
    props: {
        comment: Object
    },
    data(){
        return{
            kungFuPandaImage,
        }
    },
    components: { RouterLink }
})
</script>
