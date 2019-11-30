from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('accounts.urls')),
    path('', include('tipo_denuncia.urls')),
    path('', include('endereco_usuario.urls')),
    path('', include('denuncias.urls')),
    path('', include('usuario_denuncia.urls')),
    path('', include('all_denuncias.urls')),
    path('', include('usuario_denuncia_imagens.urls'))
]
