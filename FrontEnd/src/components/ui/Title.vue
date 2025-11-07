<template>
  <div 
    class="mini-feature-card"
    :class="{ 'mini-feature-card--clickable': clickable }"
    @click="handleClick"
  >
    <div class="mini-feature-card__image-container">
      <img 
        :src="image" 
        :alt="altText"
        class="mini-feature-card__image"
        loading="lazy"
      />
      <div class="mini-feature-card__overlay"></div>
    </div>

    <h3 class="mini-feature-card__title">
      {{ title }}
    </h3>

    <div class="mini-feature-card__glow"></div>
  </div>
</template>

<script>
export default {
  name: 'MiniFeatureCard',
  props: {
    image: {
      type: String,
      required: true,
      default: 'https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg'
    },
    altText: {
      type: String,
      default: 'Imagen descriptiva'
    },
    title: {
      type: String,
      required: true,
      default: 'Título'
    },
    clickable: {
      type: Boolean,
      default: true
    },
    to: {
      type: [String, Object],
      default: ''
    }
  },
  emits: ['click'],
  methods: {
    handleClick() {
      if (!this.clickable) return
      this.$emit('click')
      if (this.to && this.$router) {
        this.$router.push(this.to)
      }
    }
  }
}
</script>

<style scoped>
.mini-feature-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: var(--space-5);
  border-radius: var(--border-radius-lg);
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all var(--transition-normal);
  overflow: hidden;
}

.mini-feature-card--clickable {
  cursor: pointer;
}

.mini-feature-card--clickable:hover {
  transform: translateY(-6px);
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--purple-accent);
  box-shadow: var(--shadow-md);
}

/* Imagen circular */
.mini-feature-card__image-container {
  position: relative;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid transparent;
  background: linear-gradient(135deg, var(--blue-ai), var(--purple-accent));
  padding: 3px;
  margin-bottom: var(--space-4);
  transition: all var(--transition-normal);
}

.mini-feature-card--clickable:hover .mini-feature-card__image-container {
  transform: scale(1.05);
  border-color: var(--yellow-contrast);
}

.mini-feature-card__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  transition: transform var(--transition-slow);
}

.mini-feature-card--clickable:hover .mini-feature-card__image {
  transform: scale(1.1);
}

.mini-feature-card__overlay {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: linear-gradient(135deg, transparent 0%, rgba(155, 81, 224, 0.25) 100%);
  opacity: 0;
  transition: opacity var(--transition-normal);
}

.mini-feature-card--clickable:hover .mini-feature-card__overlay {
  opacity: 1;
}

/* Título */
.mini-feature-card__title {
  font-family: var(--font-family-heading);
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--text-primary);
  background: linear-gradient(135deg, var(--text-primary), var(--blue-ai));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
}

.mini-feature-card--clickable:hover .mini-feature-card__title {
  background: linear-gradient(135deg, var(--yellow-contrast), var(--pink-support));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Glow */
.mini-feature-card__glow {
  position: absolute;
  inset: 0;
  border-radius: var(--border-radius-lg);
  background: linear-gradient(135deg, var(--blue-ai), transparent, var(--purple-accent));
  opacity: 0;
  transition: opacity var(--transition-normal);
  z-index: -1;
}

.mini-feature-card--clickable:hover .mini-feature-card__glow {
  opacity: 0.1;
}

/* Responsive */
@media (max-width: 768px) {
  .mini-feature-card {
    padding: var(--space-4);
  }

  .mini-feature-card__image-container {
    width: 85px;
    height: 85px;
  }

  .mini-feature-card__title {
    font-size: var(--text-base);
  }
}
</style>
