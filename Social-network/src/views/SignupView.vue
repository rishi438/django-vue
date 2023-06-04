<template>
  <div class="max-w-7xl mx-auto grid md:grid-cols-2 grid-cols-1 gap-4">
    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <div class="mb-6 text-2xl">Sign Up</div>
        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem
          ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate.
        </p>
        <p class="font-bold">
          have an account?
          <RouterLink :to="{ name: 'login' }" class="underline"> Click here</RouterLink> to login!
        </p>
      </div>
    </div>
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6">
          <div>
            <label>Name</label><br />
            <input
              type="text"
              placeholder="Your Name"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>
          <div>
            <label>E-mail</label><br />
            <input
              type="email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Password</label><br />
            <input
              type="password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Repeat Password</label><br />
            <input
              type="password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
