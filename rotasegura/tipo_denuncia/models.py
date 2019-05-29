from django.db import models

# Create your models here.
class TipoDenuncia(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    #email = models.EmailField(max_length=100, unique=True)
    #message = models.CharField(max_length=500, blank=True)
    #owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    