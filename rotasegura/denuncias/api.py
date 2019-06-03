from denuncias.models import Denuncia
from rest_framework import viewsets, permissions
from .serializers import DenunciaSerializer

#Denuncia ViewSet
class DenunciaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = DenunciaSerializer

    queryset = Denuncia.objects.all()