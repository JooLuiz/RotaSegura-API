from usuario_denuncia.models import UsuarioDenuncia
from rest_framework import viewsets, permissions
from .serializers import UsuarioDenunciaSerializer, UsuarioDenunciaAllSerializer
from rest_framework.decorators import action

#UsuarioDenuncia ViewSet
class UsuarioDenunciaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UsuarioDenunciaSerializer

    def get_queryset(self):
        return self.request.user.usuario_denuncia.all()
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
