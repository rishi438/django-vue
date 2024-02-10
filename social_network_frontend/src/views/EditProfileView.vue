<template>
    <div class="max-w-7xl mx-auto grid grid-cols-1 gap-4">
        <div class="container mx-auto max-w-[50%]">
            <div class="p-5 bg-white border border-gray-200 rounded-lg">
                <h3 class="text-2xl text-center">Edit profile</h3>
            </div>
        </div>
        <div class="container mx-auto max-w-[50%]">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <Form class="space-y-6" :validation-schema="schema" @submit="submit_form" v-slot="{ errors }">
                    <div class="mt-2 text-stone-700">
                        <label>Name</label><br />
                        <Field name="name" class="mt-1" placeholder="Name"
                            :class="['w-full py-4 px-6 border rounded-lg ', !errors.name ?'border-gray-200':'border-red-600']" />
                        <span name="name" class="ml-2 text-red-600 text-xs line-clamp-6">{{ errors.name }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Email</label><br />
                        <Field name="email"  class="mt-1" placeholder="Email"
                        :class="['w-full py-4 px-6 border rounded-lg', !errors.email ?'border-gray-200':'border-red-600']" />
                        <span name="email" class="ml-2 text-red-600 text-xs line-clamp-6">{{ errors.email }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Current Password</label><br />
                        <Field name="c_password" class="mt-1" placeholder="Your current password"
                            :class="['w-full py-4 px-6 border rounded-lg', !errors.c_password ?'border-gray-200':'border-red-600']" />
                        <span name="c_password" class="ml-2 text-red-600 text-xs line-clamp-6">{{ errors.c_password }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>New Password</label><br />
                        <Field name="password_1" class="mt-1" placeholder="Your password"
                            :class="['w-full py-4 px-6 border rounded-lg', !errors.password_1 ?'border-gray-200':'border-red-600']" />
                        <span name="password_1" class="ml-2 text-red-600 text-xs line-clamp-6">{{ errors.password_1 }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Re-enter Password</label><br />
                        <Field name="password_2" class="mt-1" placeholder="Re-enter new password"
                            :class="['w-full py-4 px-6 border rounded-lg', !errors.password_2 ?'border-gray-200':'border-red-600']" />
                        <span name="password_2" class="ml-2 text-red-600 text-xs">{{ errors.password_2 }}</span>
                    </div>
                    <div>
                        <button class="py-3 px-6 bg-zinc-500 text-white rounded-lg">Sign up</button>
                    </div>
                </Form>
            </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import { useToastStore } from '../stores/toast'
import { useUserStore } from '../stores/user'
import { Field, Form, ErrorMessage } from 'vee-validate';

export default (await import('vue')).defineComponent({
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()
        const schema = {
            email: { required: true, email: userStore.user.email },
            name: 'required',
            c_password: 'required|minLength:8',
            password_1: 'required|minLength:8',
            password_2: 'required|minLength:8',
        };
        return {
            schema,
            toastStore,
            userStore
        }
    },
    components: {
        Field,
        Form,
        ErrorMessage
    },
    // data() {

    // },

    methods: {
        submit_form() {
            if (this.errors !== "") {
                axios
                    .post('/api/profile/edit/', this.form)
                    .then((response) => {
                        if (response.data.msg == 'User created successfully') {
                            this.toastStore.showToast(
                                5000,
                                `${response.data.msg}. Please log in`,
                                'bg-emerald-500'
                            )
                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            this.toastStore.showToast(5000, response.data.msg, 'bg-red-300')
                        }
                    })
                    .catch((error) => {
                        console.log('error', error)
                    })
            }
        }
    }
})
</script>
