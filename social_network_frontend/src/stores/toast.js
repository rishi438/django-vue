import { defineStore } from 'pinia'

export let useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        message: '',
        time: 5000,
        is_visible: false,
        status: false
    }),

    actions: {
        show_toast(message, status, time) {
            if (time) this.time = parseInt(time)
            if (status) this.status = status
            if (message) this.message = message
            this.is_visible = true
            setTimeout(() => {
                this.is_visible = false
            }, this.time)
        }
    }
})
