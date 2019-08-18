from django.db import models
from django.contrib.auth.models import User
from denuncias.models import Denuncia

class UsuarioDenuncia(models.Model):
    comentario = models.CharField(max_length=1000, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name="usuario_denuncia", on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    denuncia = models.ForeignKey(Denuncia, related_name="usuario_denuncia", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)