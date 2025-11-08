<template>
  <div class="entorno-academico">
    <div class="background__overlay"></div>

    <div class="grid-layout" v-if="!loading && !error">
      <div
        v-for="(item, index) in filteredBlocks"
        :key="item.id"
        class="grid-cell"
      >
        <FeatureCard
          class="round-img"
          :title="item.title"
          :description="item.description"
          :image="item.image_url"
          :alt-text="item.image_alt"
        />
      </div>
    </div>

    <div v-else-if="loading" class="loading">Cargando contenido...</div>
    <div v-else-if="error" class="error">Error: {{ error }}</div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'
import api from '@/services/api.js'

export default {
  name: 'EntornoAcademicoView',
  components: { FeatureCard },
  data() {
    return {
      contentBlocks: [],
      loading: true,
      error: null
    }
  },
  computed: {
    // 🔹 Solo los bloques de esta sección
    filteredBlocks() {
      return this.contentBlocks.filter(
        block => block.section === 'entorno-academico'
      )
    }
  },
  async mounted() {
    try {
      const response = await api.get('content-blocks/?section=entorno-academico')
      this.contentBlocks = response.data
    } catch (err) {
      this.error = err.message || 'Error al cargar el contenido'
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.entorno-academico {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  padding-top: 6rem; /* dejar espacio por el nav fijo */
  background: linear-gradient(to bottom right, #0b0b0b, #1a1a1a);
}

.grid-layout {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: minmax(250px, auto);
  gap: 2rem;
  padding: 3rem;
  z-index: 2;
}

/* Centrado de celdas */
.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Redondear imágenes SOLO para este view */
.round-img .feature-card__image-container {
  border-radius: 50%;
  width: 180px;
  height: 180px;
}

.round-img .feature-card__image {
  border-radius: 50%;
  object-fit: cover;
}

/* Estados */
.loading,
.error {
  text-align: center;
  margin-top: var(--space-12);
  font-size: var(--text-lg);
  color: var(--text-primary);
  opacity: 0.8;
}

.error {
  color: var(--pink-support);
}

/* Responsividad */
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
    grid-auto-rows: auto;
    gap: 1.5rem;
    padding: 1.5rem;
  }

  .grid-cell {
    justify-content: center;
  }
}
</style>
