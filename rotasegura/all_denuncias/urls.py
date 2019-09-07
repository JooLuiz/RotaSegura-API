from .api import AllDenunciasViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('api/all_denuncias', AllDenunciasViewSet)

urlpatterns = router.urls