import { defineStore } from 'pinia'

export const useMainStore = defineStore('main', {
  state: () => ({
    content: {
      title: 'IA Consciente',
      text: `Este es un proyecto que busca explorar los límites de la inteligencia artificial,
      la ética y la conciencia. En esta página encontrarás información sobre nuestras ideas,
      objetivos y avances, presentados de forma accesible y visualmente atractiva.`,
      image: 'https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg'
    }
  })
})
