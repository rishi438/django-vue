<template>
  <div class="max-w-7xl mx-auto grid grid-cols-12 gap-4">
    <div class="main-left lg:col-span-3 md:col-span-3 col-span-12 order-1">
      <div class="main-left md:col-span-1 col-span-4">
        <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
          <div class="text-center">
            <img
              src="/src/assets/1639256761455.jpeg"
              class="profile-img w-[100px] h-[100px] mb-6 rounded-full mx-auto"
            />
            <p><strong>Rishi</strong></p>
          </div>
          <div class="mt-6 flex space-x-8 justify-around">
            <p class="text-xs text-gray-500">182 friends</p>
            <p class="text-xs text-gray-500">120 posts</p>
          </div>
        </div>
      </div>
    </div>
    <div
      class="main-left lg:col-span-6 md:col-span-5 space-y-2 sm:col-span-7 col-span-12 sm:order-2 order-3"
    >
      <div class="bg-white border border-gray-200 rounded-lg">
        <div class="p-4">
          <textarea
            class="p-4 w-full bg-gray-100 rounded-lg"
            placeholder="What are you thinking about?"
          ></textarea>
        </div>
        <div class="p-4 border-t border-gray-100 flex justify-between">
          <a href="#" class="inline-block py-2 sm:px-6 px-4 bg-gray-600 text-white rounded"
            >Attach image</a
          >
          <a href="#" class="inline-block py-2 sm:px-6 px-4 bg-teal-500 text-white rounded">Post</a>
        </div>
      </div>
      <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <div class="mb-6 flex items-center justify-between">
          <div class="flex items-center space-x-6">
            <img src="../assets/1639256761455.jpeg" class="w-[40px] h-[40px] rounded-full" />
            <p><strong>Rishi</strong></p>
          </div>
          <p class="text-gray-600 text-xs">18 minutes ago</p>
        </div>
        <img
          src="https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80"
          class="w-full rounded-lg"
        />
        <div class="my-6 flex justify-between">
          <div class="flex space-x-6">
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                />
              </svg>
              <span class="text-gray-500 text-xs">82 likes</span>
            </div>
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
                />
              </svg>
              <span class="text-gray-500 text-xs">0 comments</span>
            </div>
          </div>
          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-6 h-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
              />
            </svg>
          </div>
        </div>
      </div>
      <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <div class="mb-6 flex justify-between">
          <div class="flex items-center space-x-6">
            <img src="../assets/1639256761455.jpeg" class="w-[40px] h-[40px] rounded-full" />
            <p><strong>Rishi</strong></p>
          </div>
          <div class="z-0 flex items-end">
            <p class="text-xs text-gray-600 mb-[-5px]"><span>28 minutes ago</span></p>
          </div>
        </div>
        <p>
          This is just a random text post. This is just a random text post. This is just a random
          text post. This is just a random text post.
        </p>
        <div class="my-6 flex justify-between">
          <div class="flex space-x-6">
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                />
              </svg>
              <span class="text-gray-500 text-xs">82 likes</span>
            </div>
            <div class="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z"
                />
              </svg>
              <span class="text-gray-500 text-xs">3 comments</span>
            </div>
            <div>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-6 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z"
                />
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="main-right lg:col-span-3 md:col-span-4 space-y-2 sm:col-span-5 col-span-12 sm:order-3 order-2"
    >
      <PeopleYouMayKnow />
      <Trends />
    </div>
  </div>
</template>

<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/TrendsNetwork.vue'
export default {
  name: 'FeedView',
  components: {
    PeopleYouMayKnow,
    Trends
  }
}
</script>