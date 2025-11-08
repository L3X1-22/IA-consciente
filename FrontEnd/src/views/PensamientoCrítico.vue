<template>
  <div class="pensamiento-critico">
    <div class="background__overlay"></div>

    <div class="grid-layout">
      <div
        v-for="block in contentBlocks"
        :key="block.id"
        class="grid-cell"
      >
        <FeatureCard
          class="round-img"
          :title="block.title"
          :description="block.description"
          :image="block.image_url"
          :alt="block.image_alt"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import FeatureCard from '@/components/ui/FeatureCard.vue'

export default {
  name: 'PensamientoCriticoView',
  components: { FeatureCard },
  data() {
    return {
      contentBlocks: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/content/?section=pensamiento-critico')
      this.contentBlocks = response.data
    } catch (error) {
      console.error('Error cargando los bloques de pensamiento crítico:', error)
    }
  }
}
</script>

<style scoped>
.pensamiento-critico {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  padding-top: 6rem;
  background: linear-gradient(to bottom right, #0b0b0b, #141414);
}

.grid-layout {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(250px, auto);
  gap: 2rem;
  padding: 3rem;
  position: relative;
  z-index: 2;
}

.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Imágenes redondeadas solo aquí */
.round-img .feature-card__image-container {
  border-radius: 50%;
  width: 180px;
  height: 180px;
}

.round-img .feature-card__image {
  border-radius: 50%;
  object-fit: cover;
}

/* Responsivo */
@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(200px, auto);
    padding: 2rem;
  }
}

@media (max-width: 640px) {
  .grid-layout {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 1.5rem;
  }

  .grid-cell {
    justify-content: center;
  }
}
</style>
