from rest_framework import serializers
from usuario_denuncia.models import UsuarioDenuncia
from denuncias.models import Denuncia

#AllDenuncias Serializer
class DenunciaDescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = ['descricao', 'icone']

class AllDenunciasSerializer(serializers.ModelSerializer):
    denuncia = DenunciaDescricaoSerializer()

    class Meta:
        model = UsuarioDenuncia
        fields = ['longitude', 'latitude', 'comentario', 'denuncia', 'data_hora']