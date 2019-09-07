from usuario_denuncia.models import UsuarioDenuncia
from rest_framework import viewsets, permissions
from .serializers import AllDenunciasSerializer

#Denuncia ViewSet
class AllDenunciasViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = AllDenunciasSerializer

    queryset = UsuarioDenuncia.objects.all()