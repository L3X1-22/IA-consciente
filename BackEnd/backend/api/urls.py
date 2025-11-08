from rest_framework import routers
from .views import ContentBlockViewSet, BibliographyViewSet

router = routers.DefaultRouter()
router.register(r'content-blocks', ContentBlockViewSet)
router.register(r'bibliography', BibliographyViewSet)

urlpatterns = router.urls
