from django.db import models
from usuario_denuncia.models import UsuarioDenuncia

class UsuarioDenunciaImagens(models.Model):
    usuario_denuncia = models.ForeignKey(UsuarioDenuncia, related_name="usuario_denuncia_imagens", on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=False, blank=False)