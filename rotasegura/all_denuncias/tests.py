from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from tipo_denuncia.models import TipoDenuncia

class TipoDenunciaTests(APITestCase):
    # Success Tests

    def test_create_tipoDenuncia_done(self):
        client = APIClient()

        request = client.get('/api/all_denuncias/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)