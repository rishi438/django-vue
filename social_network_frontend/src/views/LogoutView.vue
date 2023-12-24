<!-- <template></template>
<script>
import { useUserStore } from '@/stores/user'
export default {
    setup() {
        let userStore = useUserStore();
        return {
            userStore
        }
    },
    mounted(){
        this.logout()
    },
    methods: {
        async logout() {
            let removing_token = true
            try {
                await this.userStore.removeToken?.()
                await this.$router.push('/')
            } catch (error) {
                console.error('error occured: ', error)
            }
        }
    }
}
</script> -->
