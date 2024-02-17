<template>
    <div class="max-w-7xl mx-auto grid grid-cols-1 gap-4">
        <div class="container mx-auto md:max-w-[80%] lg:max-w-[50%]">
            <div class="p-5 bg-white border border-gray-200 rounded-lg">
                <h3 class="text-2xl text-center font-medium">Edit profile</h3>
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
                    ref="user_edit_form"
                >
                    <Field name="avatar" v-slot="{ handleChange, handleBlur }">
                        <label>Profile picture</label><br />
                        <img
                            :src="img_avatar"
                            class="profile-img lg:w-[150px] lg:h-[150px] md:h-[80px] md:w-[80px] mb-6 rounded-full mx-auto"
                        />

                        <label class="file-upload-wrapper">
                            <input
                                type="file"
                                class="hidden"
                                @change="
                                    ($event) => {
                                        handleChange($event, false)
                                        handle_file($event)
                                    }
                                "
                                @blur="handleBlur"
                                accept="image/*"
                            />
                            <img
                                src="/src/assets/images/clip-icon.svg"
                                class="file-upload-icon w-[25px] h-[25px] duration-300 hover:scale-75 object-contain mx-auto relative top-[5px] cursor-pointer"
                                alt="Upload image"
                            />
                        </label>
                    </Field>
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
                    <div class="mt-2 text-stone-700 px-2">
                        <input type="checkbox" class="mx-3" v-model="password_change" />
                        <label>Change Password</label>
                    </div>
                    <div class="mt-2 text-stone-700">
                        <label>New Password</label><br />
                        <Field
                            name="password1"
                            class="mt-1"
                            type="password"
                            placeholder="Your new password"
                            :disabled="!password_change"
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
                            :disabled="!password_change"
                            :class="[
                                'w-full py-4 px-6 border rounded-lg',
                                !errors.password2 ? 'border-gray-200' : 'border-red-600'
                            ]"
                        />
                        <span name="password2" class="ml-2 text-red-600 text-xs">{{
                            errors.password2
                        }}</span>
                    </div>
                    <div>
                        <button class="py-3 px-6 bg-zinc-500 text-white rounded-lg">
                            Save Changes
                        </button>
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
            name: userStore.user.name,
            current_password: null,
            password1: null,
            password2: null
        }
        const schema = {
            email: 'required:email',
            name: 'required:name',
            current_password: 'required:current password|minLength:8',
            password1: '',
            password2: ''
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
    data() {
        const img_avatar = this.userStore.user.avatar_url
        return {
            img_avatar,
            password_change: false
        }
    },
    methods: {
        read_file_as_data_URL(file) {
            return new Promise((resolve, reject) => {
                let file_reader = new FileReader()
                file_reader.onload = () => resolve(file_reader.result)
                file_reader.onerror = () => reject(file_reader.error)
                file_reader.readAsDataURL(file)
            })
        },
        async handle_file(e) {
            const file = e.target.files[0]
            const img_file = await this.file_handler(file)
            this.img_avatar = img_file
        },
        async file_handler(file) {
            if (!file) return
            try {
                let b64str = await this.read_file_as_data_URL(file)
                return b64str
            } catch (er) {
                console.error('Error reading file: ', er)
            }
        },
        submit_form(vals) {
            let form_data = new FormData()
            for (let val in vals) {
                if (vals[val] != (undefined || undefined)) form_data.append(val, vals[val])
            }
            axios
                .post(`/api/profile/${this.$route.params.id}/edit/`, form_data, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(async (response) => {
                    if (response.data.msg == 'User details updated successfully!') {
                        this.toastStore.show_toast(5000, `${response.data.msg}`, 'bg-emerald-500')
                        await this.userStore.set_attribute({
                            name: vals.name,
                            email: vals.email,
                            avatar_url: this.img_avatar
                        })
                        this.$refs.user_edit_form.resetForm()
                        this.$refs.user_edit_form.setValues({
                            email: this.userStore.user.email,
                            name: this.userStore.user.name
                        })
                    } else {
                        this.toastStore.show_toast(5000, response.data.msg, 'bg-red-300')
                    }
                })
                .catch((error) => {
                    console.log('error', error)
                })
        }
    },
    watch: {
        password_change(new_val) {
            if (new_val) {
                this.schema.password1 = 'required:password|minLength:8'
                this.schema.password2 = 'required:confirm password|minLength:8|confirmed:password1'
            } else {
                this.schema.password1 = ''
                this.schema.password2 = ''
            }
        }
    }
})
</script>
