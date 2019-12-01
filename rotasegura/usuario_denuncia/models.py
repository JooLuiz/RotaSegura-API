from django.db import models
from users.models import User
from denuncias.models import Denuncia
from datetime import datetime, timezone
from django.core.validators import MaxValueValidator

class UsuarioDenuncia(models.Model):
    comentario = models.CharField(max_length=1000, null=True, blank=True)
    usuario = models.ForeignKey(User, related_name="usuario_denuncia", on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    denuncia = models.ForeignKey(Denuncia, related_name="usuario_denuncia", on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=datetime.now, blank=True, validators=[MaxValueValidator(datetime.now(timezone.utc))])
    created_at = models.DateTimeField(auto_now_add=True)