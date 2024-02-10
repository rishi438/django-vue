<template>
  <div class="mb-6 flex justify-between">
    <div class="flex items-center space-x-6">
      <img
        src="../assets/1639256761455.jpeg"
        class="w-[40px] h-[40px] rounded-full"
      />
      <p>
        <strong>
          <RouterLink
            :to="{
              name: 'profile',
              params: { id: comment.created_by.id },
            }"
          >
            {{ comment.created_by.name }}
          </RouterLink>
        </strong>
      </p>
    </div>
    <div class="z-0 flex items-end">
      <p class="text-xs text-gray-600 mb-[-5px]">
        <span>{{ comment.created_at_formatted }} ago</span>
      </p>
    </div>
  </div>
  <p>{{ comment.body }}</p>
</template>

<script>
import { RouterLink } from "vue-router";

export default (await import("vue")).defineComponent({
  props: {
    comment: Object,
  },
  components: { RouterLink },
});
</script>
