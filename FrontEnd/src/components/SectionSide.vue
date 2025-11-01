<template>
  <section
    :class="[ 
      'w-full flex flex-col md:flex-row items-center justify-between py-16 px-10 gap-10',
      reverse ? 'md:flex-row-reverse' : '',
      bgClass
    ]"
  >
    <!-- Imagen -->
    <div class="w-full md:w-1/2 flex justify-center">
      <img
        :src="image"
        :alt="title"
        class="w-full max-w-lg rounded-2xl shadow-lg object-cover"
      />
    </div>

    <!-- Texto -->
    <div class="w-full md:w-1/2 text-center md:text-left">
      <h2 class="text-3xl font-semibold mb-4">{{ title }}</h2>
      <p class="text-gray-700 text-lg leading-relaxed">{{ text }}</p>
    </div>
  </section>
</template>

<script>
export default {
  name: "SectionSide", // 👈 nombre corregido
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

img {
  transition: transform 0.3s ease;
}

img:hover {
  transform: scale(1.03);
}
</style>
