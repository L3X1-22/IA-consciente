from rest_framework import serializers
from .models import ContentBlock, Bibliography

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'

class BibliographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliography
        fields = '__all__'
