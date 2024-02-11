<template>
    <div class="max-w-7xl mx-auto grid md:grid-cols-2 grid-cols-1 gap-4">
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <div class="mb-6 text-2xl">Sign Up</div>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit
                    mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor
                    sit mate.
                </p>
                <p class="font-bold">
                    have an account?
                    <RouterLink :to="{ name: 'login' }" class="underline"> Click here</RouterLink>
                    to login!
                </p>
            </div>
        </div>
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submit_form">
                    <div>
                        <label>Name</label><br />
                        <input
                            type="text"
                            placeholder="Your Name"
                            v-model="form.name"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>
                    <div>
                        <label>E-mail</label><br />
                        <input
                            type="email"
                            placeholder="Your e-mail address"
                            v-model="form.email"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>
                    <div>
                        <label>Password</label><br />
                        <input
                            type="password"
                            placeholder="Your password"
                            v-model="form.password"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>
                    <div>
                        <label>Repeat Password</label><br />
                        <input
                            type="password"
                            placeholder="Your password"
                            v-model="form.confirm_password"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
                        />
                    </div>
                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>
                    <div>
                        <button class="py-3 px-6 bg-zinc-500 text-white rounded-lg">Sign up</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useToastStore } from '../stores/toast'

export default (await import('vue')).defineComponent({
    name: 'SignupView',
    setup() {
        const toastStore = useToastStore();
        return {
            toastStore
        };
    },
    data() {
        return {
            form: {
                email: '',
                name: '',
                password: '',
                confirm_password: ''
            },
            errors: []
        };
    },
    methods: {
        submit_form() {
            this.error = [];
            let email_regex = /^[a-zA-Z0-9,_+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (email_regex.test(this.form.email)) {
                this.errors.push('Your e-mail is missing or invalid');
            }
            if (this.form.name === '') {
                this.errors.push('Your name is missing');
            }
            if (this.form.password === '') {
                this.errors.push('Your password is missing');
            }
            if (this.form.password !== this.form.confirm_password) {
                this.errors.push('Your password does not match');
            }
            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then((response) => {
                        if (response.data.msg == 'User created successfully') {
                            this.toastStore.show_toast(
                                5000,
                                `${response.data.msg}. Please log in`,
                                'bg-emerald-500'
                            );
                            this.form.email = '';
                            this.form.name = '';
                            this.form.password = '';
                            this.form.confirm_password = '';
                        } else {
                            this.toastStore.show_toast(5000, response.data.msg, 'bg-red-300');
                        }
                    })
                    .catch((error) => {
                        console.log('error', error);
                    })
            }
        }
    }
});
</script>
