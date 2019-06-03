from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('tipo_denuncia.urls')),
    path('', include('endereco_usuario.urls'))
]
