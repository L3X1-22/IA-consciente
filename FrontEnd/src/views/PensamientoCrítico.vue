<template>
  <div class="pensamiento-critico">
    <div class="background__overlay"></div>

    <div class="grid-layout">
      <!-- Fila 1 -->
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Reconoce tus límites"
          description="Cuando usas un LLM, pregúntate si podrías haber llegado a esa idea sola. Si no, investiga antes de aceptar la respuesta."
          image="https://images.unsplash.com/photo-1581090700227-1e37b190418e?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Evalúa la coherencia"
          description="Un modelo puede sonar convincente, pero no siempre tiene razón. Verifica los datos y busca contradicciones."
          image="https://images.unsplash.com/photo-1521791055366-0d553872125f?auto=format&fit=crop&w=800&q=80"
        />
      </div>

      <!-- Fila 2 -->
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Haz pausas conscientes"
          description="Si notas que el modelo escribe por ti sin que reflexiones, haz una pausa y vuelve a pensar en lo que querías comunicar."
          image="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>

      <!-- Fila 3 -->
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Compara perspectivas"
          description="Usar un LLM no debe reemplazar la diversidad de pensamiento. Contrasta sus respuestas con opiniones humanas reales."
          image="https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80"
        />
      </div>
      <div class="grid-cell"></div>
      <div class="grid-cell">
        <FeatureCard
          class="round-img"
          title="Recupera la autoría"
          description="Asegúrate de que tu voz siga presente en lo que creas con ayuda de IA. No dejes que piense por ti."
          image="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80"
        />
      </div>
    </div>
  </div>
</template>

<script>
import FeatureCard from '@/components/ui/FeatureCard.vue'

export default {
  name: 'PensamientoCriticoView',
  components: { FeatureCard }
}
</script>

<style scoped>
.pensamiento-critico {
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow-y: auto;
  padding-top: 6rem; /* deja espacio por el nav fijo */
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
