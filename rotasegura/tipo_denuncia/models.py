from django.db import models

# Create your models here.
class TipoDenuncia(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    icone = models.CharField(max_length=200, default='exclamation-triangle')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    