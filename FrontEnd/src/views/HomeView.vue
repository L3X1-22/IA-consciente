<template>
  <div class="home">
    <!-- Imagen de fondo con máscara -->
    <div class="background">
      <div class="background__overlay"></div>

      <!-- Grid principal -->
      <div class="grid-layout">

        <!-- Fila 2 vacía -->
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>
        <div class="grid-cell"></div>

        <!-- Fila 1: SimpleTextBlock centrado -->
        <div class="grid-cell"></div>
        <div class="grid-cell grid-center">
          <SimpleTextBlock title="IA consciente"
            text="La IA está en todos lados: en tus redes, en tus playlists, en asistentes virtuales. Es poderosa... Pero también puede influir en cómo piensas y lo que haces. Por eso, usar IA con conciencia es clave. Aquí te mostramos cómo entenderla, cuestionarla y aprovecharla sin perder tu pensamiento crítico. Porque la inteligencia artificial no debería sustituir tu esencia, sino potenciarla." />
        </div>
        <div class="grid-cell"></div>

        <Title title="Introducción a la Inteligencia Artificial"
          image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          :to="'/que-es-ia'" />

        <Title title="Cómo funciona un Modelo de Lenguaje"
          image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          :to="'/como-funciona-un-llm'" />

        <Title title="IA en la Educación y el Entorno Académico"
          image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          :to="'/entorno-academico'" />

        <Title title="Pensamiento Crítico frente a la Inteligencia Artificial"
          image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          :to="'/pensamiento-critico'" />

      </div>
    </div>
  </div>
</template>

<script>
import Title from '@/components/ui/Title.vue'
import SimpleTextBlock from '@/components/ui/SimpleTextBlock.vue'

export default {
  name: 'HomeView',
  components: { Title, SimpleTextBlock }
}
</script>

<style scoped>
.home {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  /* sin scroll en desktop/tablet */
}

/* Fondo */
.background {
  position: relative;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1920&q=80') center center / cover no-repeat;
}

.background__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.5) 0%, transparent 100%);
  z-index: 1;
}

/* Grid principal */
.grid-layout {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(150px, auto);
  height: 100%;
  width: 100%;
  padding: 6rem 3rem 3rem;
  /* 🔹 deja espacio arriba para el nav fijo */
  gap: 1.5rem;
  box-sizing: border-box;
  align-items: stretch;
}

.grid-cell:has(> Title) {
  align-self: stretch;
}

.grid-cell>* {
  width: 100%;
  height: 100%;
}

/* Celdas */
.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

.grid-cell img {
  object-fit: cover;
  width: 100%;
  height: 100%;
  border-radius: 1rem;
}

/* Centrado del bloque de texto */
.grid-center {
  justify-content: center;
  align-items: center;
  text-align: center;
  grid-column: 2 / span 2;
}

/* Celdas vacías solo visibles en escritorio */
.grid-cell:empty {
  display: block;
}

/* --- Tablet --- */
@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    padding: 5rem 2rem 2rem;
    /* ajusta espacio bajo el nav */
    gap: 1rem;
  }

  .grid-cell:empty {
    display: none;
  }

  .grid-center {
    grid-column: 1 / span 2;
  }
}

/* --- Móvil --- */
@media (max-width: 640px) {
  .home {
    height: auto;
    /* 🔹 permite scroll */
    min-height: 100vh;
    overflow-y: auto;
    /* 🔹 activa scroll vertical */
  }

  .grid-layout {
    grid-template-columns: 1fr;
    padding: 5rem 1.5rem 1.5rem;
    /* 🔹 baja el contenido para el nav fijo */
    gap: 1rem;
  }

  .grid-cell:empty {
    display: none;
  }

  .grid-center {
    grid-column: 1;
  }
}
</style>
