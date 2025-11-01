<template>
  <div class="home">
    <img
      src="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
      alt="Logo del proyecto"
      class="logo"
    />

    <h1>Bienvenida al proyecto 🩵</h1>
    <p>Tu aplicación Vue ya está funcionando correctamente.</p>

    <!-- Sección lateral -->
    <SectionSide
      title="Nuestra Misión"
      text="Exploramos el futuro de la creación de contenido con inteligencia artificial."
      image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
    />

    <!-- Sección invertida con fondo gris -->
    <SectionDown
      title="Visión"
      text="Crear herramientas accesibles que impulsen la creatividad humana con tecnología."
      image="https://comunicagenia.com/wp-content/uploads/2024/10/usar-inteligencia-artificial-creador-contenido-1080x675.jpg"
      :reverse="true"
      bg="gray"
    />
  </div>
</template>

<script>
import SectionSide from "@/components/SectionSide.vue";
import SectionDown from "@/components/SectionDown.vue";

export default {
  name: "HomeView",
  components: {
    SectionSide,
    SectionDown
  }
};
</script>

<style>
.home {
  text-align: center;
  margin-top: 50px;
  font-family: 'Arial', sans-serif;
}

.logo {
  width: 1000px;
  height: auto;
  margin-bottom: 20px;
}
</style>
