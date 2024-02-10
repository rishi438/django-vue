<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h3 class="mb-6 text-xl">Trends</h3>
        <div class="space-y-4">
            <div class="flex items-center justify-between" v-for="trend in trends" :key="trend.id">
                <div class="flex items-center space-x-2">
                    <p class="text-xs">
                        <strong>#{{ trend.hashtag }}</strong><br />
                        <span class="text-gray-500">{{ trend.occurences }} posts</span>
                    </p>
                </div>
                <RouterLink :to="{ name: 'trends', params: { id: trend.hashtag } }" class="py-2 px-3
           bg-teal-500 text-white text-xs rounded-lg">Explore</RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default (await import('vue')).defineComponent({
    name: 'trends',
    data() {
        return {
            trends: []
        }
    },
    mounted() {
        this.get_trends()
    },
    methods: {
        get_trends() {
            axios
                .get('/api/post/trends/')
                .then(res => {
                    this.trends = res.data
                })
                .catch(err => {
                    console.error("Error occured: ", err)
                })
        }
    }
})
</script>
