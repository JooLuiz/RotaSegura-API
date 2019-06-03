from rest_framework import serializers
from usuario_denuncia.models import UsuarioDenuncia

#UsuarioDenuncia Serializer

class UsuarioDenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDenuncia
        fields = '__all__'