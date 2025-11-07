<template>
    <section class="text-block">
        <h2 class="text-block__title">{{ title }}</h2>
        <p class="text-block__paragraph">{{ text }}</p>
    </section>
</template>

<script>
export default {
    name: "SimpleTextBlock",
    props: {
        title: {
            type: String,
            required: true
        },
        text: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.text-block {
    text-align: center;
    padding: var(--space-8, 2rem);
    color: var(--text-primary, #fff);
    background: rgba(0, 0, 0, 0.6);
    /* negro translúcido */
    border-radius: 1rem;
    /* bordes redondeados */
    padding: 2rem;
    /* espacio interior */
    text-align: center;
    /* centrar texto */
    color: white;
    /* texto claro */
    backdrop-filter: blur(5px);
}

.text-block__title {
    font-family: var(--font-family-heading, 'Poppins', sans-serif);
    font-size: var(--text-3xl, 2rem);
    margin-bottom: var(--space-4, 1rem);
    background: linear-gradient(135deg, var(--blue-ai, #6dcff6), var(--purple-accent, #9b51e0));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.text-block__paragraph {
    font-family: var(--font-family-primary, 'Inter', sans-serif);
    font-size: var(--text-base, 1rem);
    line-height: 1.6;
    opacity: 0.9;
    max-width: 700px;
    margin: 0 auto;
}
</style>
