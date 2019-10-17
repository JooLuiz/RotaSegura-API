from django.db import models
from users.models import User

class EnderecoUsuario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=600, null=True)
    usuario = models.ForeignKey(User, related_name="endereco_usuario", on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)