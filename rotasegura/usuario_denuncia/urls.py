from rest_framework import routers
from .api import UsuarioDenunciaViewSet
from .api_all import UsuarioDenunciaAllViewSet

router = routers.DefaultRouter()
router.register('api/usuario_denuncia', UsuarioDenunciaViewSet, 'usuario_denuncia')
router.register('api/usuario_denuncia_all', UsuarioDenunciaAllViewSet, 'usuario_denuncia_all')

urlpatterns = router.urls