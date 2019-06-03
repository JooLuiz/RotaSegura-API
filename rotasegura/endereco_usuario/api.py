from endereco_usuario.models import EnderecoUsuario
from rest_framework import viewsets, permissions
from .serializers import EnderecoUsuarioSerializer

#EnderecoUsuario ViewSet
class EnderecoUsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = EnderecoUsuarioSerializer

    def get_queryset(self):
        return self.request.User.endereco_usuario.all()
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.User)