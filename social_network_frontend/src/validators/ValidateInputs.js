import { defineRule } from 'vee-validate'

defineRule('required', (value, check) => {
    if (!value || !value.length) {
        return `${check} is required`
    }
    return true
})

defineRule('email', (val) => {
    if (!val || !val.length) {
        return true
    }
    if (!/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/.test(val)) {
        return 'This field must be a valid email'
    }
    return true
})

defineRule('minLength', (value, [limit]) => {
    if (!value || !value.length) {
        return true
    }
    if (value.length < limit) {
        return `This field must be at least ${limit} characters`
    }
    return true
})

defineRule('confirmed', (value, [target], ctx) => {
    if (value === ctx.form[target]) {
        return true
    }
    return 'Passwords must match'
})
