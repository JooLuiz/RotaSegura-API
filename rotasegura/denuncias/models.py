from django.db import models
from tipo_denuncia.models import TipoDenuncia

class Denuncia(models.Model):
    descricao = models.CharField(max_length=1000)
    tipo_denuncia = models.ForeignKey(TipoDenuncia, related_name="denuncias", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)