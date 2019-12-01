from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('accounts.urls')),
    path('', include('tipo_denuncia.urls')),
    path('', include('endereco_usuario.urls')),
    path('', include('denuncias.urls')),
    path('', include('usuario_denuncia.urls')),
    path('', include('all_denuncias.urls')),
    path('', include('usuario_denuncia_imagens.urls')),
    path('', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)))
]
