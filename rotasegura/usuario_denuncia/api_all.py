from usuario_denuncia.models import UsuarioDenuncia
from rest_framework import viewsets, permissions
from .serializers import UsuarioDenunciaSerializer, UsuarioDenunciaAllSerializer
from rest_framework.decorators import action

class UsuarioDenunciaAllViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    serializer_class = UsuarioDenunciaAllSerializer

    queryset = UsuarioDenuncia.objects.all()