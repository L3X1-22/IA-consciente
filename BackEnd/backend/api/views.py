from rest_framework import viewsets
from .models import ContentBlock, Bibliography
from .serializers import ContentBlockSerializer, BibliographySerializer

class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class BibliographyViewSet(viewsets.ModelViewSet):
    queryset = Bibliography.objects.all()
    serializer_class = BibliographySerializer
