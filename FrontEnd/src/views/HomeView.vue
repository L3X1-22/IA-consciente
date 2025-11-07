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
          <SimpleTextBlock
            title="IA consciente"
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer malesuada ex ut ligula eleifend, eget tincidunt turpis suscipit. Suspendisse potenti. Proin dapibus diam et justo convallis, sed tincidunt purus tincidunt."
          />
        </div>
        <div class="grid-cell"></div>

        <!-- Fila 3: los 4 Title.vue -->
        <div class="grid-cell">
          <Title
            title="Primero"
            image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          />
        </div>
        <div class="grid-cell">
          <Title
            title="Segundo"
            image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          />
        </div>
        <div class="grid-cell">
          <Title
            title="Tercero"
            image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          />
        </div>
        <div class="grid-cell">
          <Title
            title="Cuarto"
            image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
          />
        </div>
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
}

/* Fondo con imagen y máscara negra degradada */
.background {
  position: relative;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1920&q=80')
    center center / cover no-repeat;
}

.background__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.5) 0%, transparent 100%);
  z-index: 1;
}

/* Grid principal */
.grid-layout {
    padding-top: 5rem;
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: none;
  grid-auto-rows: minmax(150px, auto);
  height: 100%;
  width: 100%;
  padding: 3rem;
  gap: 1.5rem;
  box-sizing: border-box;
}

/* Celdas genéricas */
.grid-cell {
  display: flex;
  justify-content: center;
  align-items: center;
}

.grid-cell:empty {
  display: block;
}


/* Centrado del bloque de texto */
.grid-center {
  justify-content: center;
  align-items: center;
  text-align: center;
  grid-column: 2 / span 2;
}

@media (max-width: 1024px) {
  .grid-layout {
    grid-template-columns: repeat(2, 1fr);
    grid-auto-rows: minmax(150px, auto);
    padding-top: 3rem;
  }

  /* Ocultar celdas vacías */
  .grid-cell:empty {
    display: none;
  }

  .grid-center {
    grid-column: 1 / span 2;
  }
}

/* Móvil (hasta 640px): sin celdas vacías, grid fluido */
@media (max-width: 640px) {
  .grid-layout {
    grid-template-columns: 1fr;
    padding-top: 1rem;
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
