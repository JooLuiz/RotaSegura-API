from rest_framework import serializers
from usuario_denuncia_imagens.models import UsuarioDenunciaImagens

#UsuarioDenunciaImagens Serializer

class UsuarioDenunciaImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDenunciaImagens
        fields = '__all__'