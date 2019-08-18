from rest_framework import serializers
from denuncias.models import Denuncia

#DenunciaLead Serializer

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'