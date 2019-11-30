from usuario_denuncia_imagens.models import UsuarioDenunciaImagens
from rest_framework import viewsets, permissions
from .serializers import UsuarioDenunciaImagensSerializer

#UsuarioDenuncia ViewSet
class UsuarioDenunciaImagensViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = UsuarioDenunciaImagensSerializer

    def get_queryset(self):
        return self.request.user.usuario_denuncia.usuario_denuncia_imagens.all()
