from django.db import models


class ContentBlock(models.Model):
    FEATURE = 'feature-card'
    TEXT = 'simple-text-block'
    TYPES = [
        (FEATURE, 'Feature Card'),
        (TEXT, 'Simple Text Block'),
    ]

    SECTION_CHOICES = [
        ('home', 'Home'),
        ('que-es-ia', 'Qué es la IA'),
        ('como-funciona-un-llm', 'Cómo funciona un LLM'),
        ('entorno-academico', 'Entorno académico'),
        ('pensamiento-critico', 'Pensamiento crítico'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    type = models.CharField(max_length=30, choices=TYPES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['section', 'order']

    def __str__(self):
        return f"{self.section} → {self.title}"


class Bibliography(models.Model):
    title = models.CharField(help_text="Titulo del articulo", max_length=255)
    author = models.CharField(help_text="Autor del articulo", max_length=255, blank=True)
    year = models.CharField(help_text="Año de publicación del articulo", max_length=10, blank=True)
    source_url = models.URLField(help_text="Link del articulo original (una dirección tipo https://scholar.google.com/)", blank=True)
    reference_text = models.TextField(help_text="Texto completo de la referencia (APA o similar).", blank=True)

    # Si quieres relacionarla con una sección del sitio:
    section = models.CharField(
        max_length=50,
        choices=ContentBlock.SECTION_CHOICES,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bibliografía"
        ordering = ['section', 'author']

    def __str__(self):
        return f"{self.title} ({self.year})"
