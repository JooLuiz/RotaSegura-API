from rest_framework import serializers
from endereco_usuario.models import EnderecoUsuario

#EnderecoUsuario Serializer

class EnderecoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoUsuario
        fields = '__all__'