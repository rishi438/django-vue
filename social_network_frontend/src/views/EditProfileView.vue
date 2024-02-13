<template>
    <div class="max-w-7xl mx-auto grid grid-cols-1 gap-4">
        <div class="container mx-auto md:max-w-[80%] lg:max-w-[50%]">
            <div class="p-5 bg-white border border-gray-200 rounded-lg">
                <h3 class="text-2xl text-center">Edit profile</h3>
            </div>
        </div>
        <div class="container mx-auto md:max-w-[80%] lg:max-w-[50%]">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <Form
                    class="space-y-6"
                    :validation-schema="schema"
                    @submit="submit_form"
                    v-slot="{ errors }"
                    :initial-values="initial_values"
                    ref="my_form"
                >
                    <div class="mt-2 text-stone-700">
                        <label>Name</label><br />
                        <Field
                            name="name"
                            class="mt-1"
                            placeholder="Name"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg ',
                                !errors.name ? 'border-gray-200' : 'border-red-600'
                            ]"
                        />
                        <span name="name" class="ml-2 text-red-600 text-xs line-clamp-6">{{
                            errors.name
                        }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Email</label><br />
                        <Field
                            name="email"
                            class="mt-1"
                            type="email"
                            placeholder="Email"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg',
                                !errors.email ? 'border-gray-200' : 'border-red-600'
                            ]"
                        />
                        <span name="email" class="ml-2 text-red-600 text-xs line-clamp-6">{{
                            errors.email
                        }}</span>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Current Password</label><br />
                        <Field
                            name="current_password"
                            class="mt-1"
                            type="password"
                            placeholder="Your current password"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg',
                                !errors.current_password ? 'border-gray-200' : 'border-red-600'
                            ]"
                        />
                        <span
                            name="current_password"
                            class="ml-2 text-red-600 text-xs line-clamp-6"
                        >
                            {{ errors.current_password }}</span
                        >
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>New Password</label><br />
                        <Field
                            name="password1"
                            class="mt-1"
                            type="password"
                            placeholder="Your new password"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg',
                                !errors.password1 ? 'border-gray-200' : 'border-red-600'
                            ]"
                        />
                        <span name="password1" class="ml-2 text-red-600 text-xs line-clamp-6">
                            {{ errors.password1 }}</span
                        >
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>Confirm Password</label><br />
                        <Field
                            name="password2"
                            type="password"
                            class="mt-1"
                            placeholder="Confirm new password"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg',
                                !errors.password2 ? 'border-gray-200' : 'border-red-600'
                            ]"
                            :data-vv-as="'password1'"
                        />
                        <span name="password2" class="ml-2 text-red-600 text-xs">{{
                            errors.password2
                        }}</span>
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
import { Field, Form } from 'vee-validate'

export default (await import('vue')).defineComponent({
    setup() {
        const toastStore = useToastStore()
        const userStore = useUserStore()
        const initial_values = {
            email: userStore.user.email,
            name: userStore.user.name
        }
        const schema = {
            email: { required: true },
            name: 'required',
            current_password: 'required|minLength:8',
            password1: 'required|minLength:8',
            password2: 'required:true|minLength:8|confirmed:password1'
        }
        return {
            schema,
            toastStore,
            userStore,
            initial_values
        }
    },
    components: {
        Field,
        Form
    },
    methods: {
        submit_form(vals) {
            axios
                .post(`/api/profile/${this.$route.params.id}/edit/`, vals)
                .then((response) => {
                    if (response.data.msg == 'User created successfully') {
                        this.toastStore.show_toast(
                            5000,
                            `${response.data.msg}. Please log in`,
                            'bg-emerald-500'
                        )
                    } else {
                        this.toastStore.show_toast(5000, response.data.msg, 'bg-red-300')
                    }
                })
                .catch((error) => {
                    console.log('error', error)
                })
        }
    }
})
</script>
