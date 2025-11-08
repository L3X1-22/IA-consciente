<template>
  <div class="que-es-ia-view">
    <div class="content-grid" v-if="!loading && !error">
      <component
        v-for="(item, index) in filteredBlocks"
        :is="item.type === 'feature-card' ? 'FeatureCard' : 'SimpleTextBlock'"
        :key="item.id"
        :title="item.title"
        :description="item.description"
        :text="item.description"
        :image="item.image_url"
        :alt-text="item.image_alt"
        :reverse="index % 2 !== 0 && item.type === 'feature-card'"
        class="fade-in content-item"
      />
    </div>

    <div v-else-if="loading" class="loading">Cargando contenido...</div>
    <div v-else-if="error" class="error">Error: {{ error }}</div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'
import SimpleTextBlock from '@/components/ui/SimpleTextBlock.vue'
import api from '@/services/api.js'

export default {
  name: 'QueEsIAView',
  components: {
    FeatureCard,
    SimpleTextBlock
  },
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
        block => block.section === 'que-es-ia'
      )
    }
  },
  async mounted() {
    try {
      const response = await api.get('content-blocks/?section=que-es-ia')
      this.contentBlocks = response.data
    } catch (err) {
      this.error = err.message || 'Error al cargar los bloques de contenido'
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.que-es-ia-view {
  width: 100%;
  min-height: 100vh;
  padding-top: 90px;
  background: var(--bg-primary);
  color: var(--text-primary);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  justify-content: center;
  animation: fadeIn 0.6s ease-out;
}

/* 🧩 Grid adaptable y simétrica */
.content-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-12);
  max-width: 1200px;
  width: 100%;
  padding: var(--space-8) var(--space-6);
}

/* 🟰 Cada item mantiene el mismo espacio vertical */
.content-item {
  display: flex;
  justify-content: center;
  align-items: stretch;
  min-height: 280px;
}

/* Alternancia de orientación */
.content-grid > *:nth-child(odd) .feature-card {
  flex-direction: row;
}
.content-grid > *:nth-child(even) .feature-card {
  flex-direction: row-reverse;
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
</style>
