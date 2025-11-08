<template>
  <div class="llm-view">
    <div v-if="!loading && !error" class="grid-llm">
      <!-- 🔹 Texto izquierdo -->
      <div
        class="llm-text left"
        v-if="filteredBlocks[0]"
      >
        <SimpleTextBlock
          :title="filteredBlocks[0].title"
          :text="filteredBlocks[0].description"
        />
      </div>

      <!-- 🔹 Imagen central (hardcodeada) -->
      <div class="llm-image">
        <img
          src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1920&q=80"
          alt="Red neuronal representando un modelo de lenguaje"
        />
      </div>

      <!-- 🔹 Texto derecho -->
      <div
        class="llm-text right"
        v-if="filteredBlocks[1]"
      >
        <SimpleTextBlock
          :title="filteredBlocks[1].title"
          :text="filteredBlocks[1].description"
        />
      </div>

      <!-- 🔹 Texto inferior -->
      <div
        class="llm-text bottom"
        v-if="filteredBlocks[2]"
      >
        <SimpleTextBlock
          :title="filteredBlocks[2].title"
          :text="filteredBlocks[2].description"
        />
      </div>
    </div>

    <!-- Estados -->
    <div v-else-if="loading" class="loading">Cargando contenido...</div>
    <div v-else-if="error" class="error">Error: {{ error }}</div>
  </div>
</template>

<script>
import SimpleTextBlock from '@/components/ui/SimpleTextBlock.vue'
import api from '@/services/api.js'

export default {
  name: 'ComoFuncionaLLMView',
  components: {
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
    filteredBlocks() {
      // 🔹 Asegura que solo muestre los de esta sección
      return this.contentBlocks.filter(
        block => block.section === 'como-funciona-un-llm'
      )
    }
  },
  async mounted() {
    try {
      const response = await api.get('content-blocks/?section=como-funciona-un-llm')
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
.llm-view {
  width: 100%;
  min-height: 100vh;
  padding-top: 90px;
  background: radial-gradient(circle at center, #0d0d0d 0%, #121212 100%);
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.grid-llm {
  display: grid;
  grid-template-columns: 1fr 1.2fr 1fr;
  grid-template-rows: auto auto;
  gap: 2rem;
  max-width: 1400px;
  width: 100%;
  padding: 2rem;
  align-items: center;
}

/* Imagen central */
.llm-image {
  grid-column: 2 / span 1;
  grid-row: 1 / span 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.llm-image img {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 1rem;
  object-fit: cover;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.4);
  transition: transform 0.4s ease;
}

.llm-image img:hover {
  transform: scale(1.03);
}

/* Posiciones */
.llm-text.left {
  grid-column: 1;
  grid-row: 1;
}

.llm-text.right {
  grid-column: 3;
  grid-row: 1;
}

.llm-text.bottom {
  grid-column: 1 / span 3;
  grid-row: 2;
  display: flex;
  justify-content: center;
}

/* Responsivo - tablet */
@media (max-width: 1024px) {
  .grid-llm {
    grid-template-columns: 1fr 1fr;
  }

  .llm-text.left {
    grid-column: 1;
    grid-row: 1;
  }

  .llm-image {
    grid-column: 2;
    grid-row: 1;
  }

  .llm-text.right {
    grid-column: 1 / span 2;
    grid-row: 2;
  }

  .llm-text.bottom {
    grid-column: 1 / span 2;
    grid-row: 3;
  }
}

/* Responsivo - móvil */
@media (max-width: 768px) {
  .grid-llm {
    grid-template-columns: 1fr;
  }

  .llm-text.left,
  .llm-text.right,
  .llm-text.bottom,
  .llm-image {
    grid-column: 1;
  }

  .llm-text.left {
    grid-row: 1;
  }

  .llm-image {
    grid-row: 2;
  }

  .llm-text.right {
    grid-row: 3;
  }

  .llm-text.bottom {
    grid-row: 4;
  }

  .llm-image img {
    max-width: 100%;
  }
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
