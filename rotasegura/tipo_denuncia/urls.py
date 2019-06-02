from rest_framework import routers
from .api import TipoDenunciaViewSet

router = routers.DefaultRouter()
router.register('api/tipodenuncia', TipoDenunciaViewSet, 'tipo_denuncia')

urlpatterns = router.urls