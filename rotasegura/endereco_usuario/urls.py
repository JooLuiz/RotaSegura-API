from rest_framework import routers
from .api import EnderecoUsuarioViewSet

router = routers.DefaultRouter()
router.register('api/endereco_usuario', EnderecoUsuarioViewSet, 'endereco_usuario')

urlpatterns = router.urls