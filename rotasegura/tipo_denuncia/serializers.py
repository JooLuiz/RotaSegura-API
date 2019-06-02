from rest_framework import serializers
from tipo_denuncia.models import TipoDenuncia

#TipoDenuncia Serializer

class TipoDenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDenuncia
        fields = '__all__'