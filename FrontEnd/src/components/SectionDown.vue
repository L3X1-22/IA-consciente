<template>
  <section
    :class="[
      'w-full flex flex-col md:items-center justify-center py-16 px-6 gap-8',
      reverse ? 'md:flex-row-reverse' : 'md:flex-row',
      bgClass
    ]"
  >
    <!-- Imagen -->
    <img
      :src="image"
      :alt="title"
      class="w-1/3 md:w-1/4 rounded-2xl shadow-lg"
    />

    <!-- Texto -->
    <div class="md:w-1/2 text-center md:text-left">
      <h2 class="text-3xl font-semibold mb-4">{{ title }}</h2>
      <p class="text-gray-700 mb-4">{{ text }}</p>
    </div>
  </section>
</template>

<script>
export default {
  name: "Section",
  props: {
    title: String,
    text: String,
    image: String,
    reverse: {
      type: Boolean,
      default: false
    },
    bg: {
      type: String,
      default: "white"
    }
  },
  computed: {
    bgClass() {
      if (this.bg === "gray") return "bg-gray-100";
      if (this.bg === "dark") return "bg-gray-800 text-white";
      return "bg-white";
    }
  }
};
</script>

<style scoped>
section {
  transition: all 0.3s ease;
}
</style>