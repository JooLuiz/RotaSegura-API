from rest_framework import routers
from .api import UsuarioDenunciaViewSet

router = routers.DefaultRouter()
router.register('api/usuario_denuncia', UsuarioDenunciaViewSet, 'usuario_denuncia')

urlpatterns = router.urls