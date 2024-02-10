import { defineStore } from 'pinia'

export let useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),
    actions: {
        show_toast(ms, message, classes) {
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true
            setTimeout(() => {
                this.classes += ' -translate-y-28'
            }, 10)
            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '')
            }, this.ms - 500)

            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})
