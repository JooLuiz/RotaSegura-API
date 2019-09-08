from tipo_denuncia.models import TipoDenuncia
from rest_framework import viewsets, permissions
from .serializers import TipoDenunciaSerializer

#TipoDenuncia ViewSet
class TipoDenunciaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    queryset = TipoDenuncia.objects.all()

    serializer_class = TipoDenunciaSerializer