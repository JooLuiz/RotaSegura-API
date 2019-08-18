from rest_framework import routers
from .api import DenunciaViewSet

router = routers.DefaultRouter()
router.register('api/denuncias', DenunciaViewSet, 'denuncias')

urlpatterns = router.urls