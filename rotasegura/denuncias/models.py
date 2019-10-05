from django.db import models
from tipo_denuncia.models import TipoDenuncia

class Denuncia(models.Model):
    descricao = models.CharField(max_length=1000)
    tipo_denuncia = models.ForeignKey(TipoDenuncia, related_name="denuncias", on_delete=models.CASCADE)
    icone = models.CharField(max_length=200, default='exclamation-triangle')
    created_at = models.DateTimeField(auto_now_add=True)