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

    # def get_queryset(self):
    #     return self.request.User.leads.all()
    
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.User)