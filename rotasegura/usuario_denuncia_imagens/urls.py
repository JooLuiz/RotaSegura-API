from rest_framework import routers
from .api import UsuarioDenunciaImagensViewSet

router = routers.DefaultRouter()
router.register('api/usuario_denuncia_imagens', UsuarioDenunciaImagensViewSet, 'usuario_denuncia_imagens')

urlpatterns = router.urls