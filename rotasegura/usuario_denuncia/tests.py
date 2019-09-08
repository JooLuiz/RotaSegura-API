from django.contrib.auth.models import User
from denuncias.models import Denuncia
from usuario_denuncia.models import UsuarioDenuncia
from tipo_denuncia.models import TipoDenuncia
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class UsuarioDenunciaTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testes', password='123', email='testes@email.com')
        user.save()
        tipoDenuncia = TipoDenuncia.objects.create(descricao='TipoDenunciaTest')
        tipoDenuncia.save()
        denuncia = Denuncia.objects.create(descricao='DenunciaTest', tipo_denuncia=tipoDenuncia)
        denuncia.save()

    # Success Tests

    def test_create_usuario_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')
        client.force_authenticate(user=user)

        data = {'comentario': 'Test 1', 'latitude': '1', 'longitude': '1', 'denuncia': str(denuncia.id)}
        request = client.post('/api/usuario_denuncia/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UsuarioDenuncia.objects.count(), 1)
        self.assertEqual(UsuarioDenuncia.objects.get().comentario, 'Test 1')
    
    def test_update_usuario_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')
        client.force_authenticate(user=user)

        usuarioDenuncia = UsuarioDenuncia.objects.create(comentario='Test 2', latitude='1', longitude='1', denuncia=denuncia)
        usuarioDenuncia.save()
        data = {'comentario': 'Test Update', 'latitude': '1', 'longitude': '1', 'denuncia': str(denuncia.id)}
        request = client.put('/api/usuario_denuncia/'+str(usuarioDenuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(UsuarioDenuncia.objects.count(), 1)
        self.assertEqual(UsuarioDenuncia.objects.get().comentario, 'Test Update')

    def test_delete_usuario_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')
        client.force_authenticate(user=user)

        usuarioDenuncia = UsuarioDenuncia.objects.create(comentario='Test 3', latitude='1', longitude='1', denuncia=denuncia)
        usuarioDenuncia.save()
        request = client.delete('/api/usuario_denuncia/'+str(usuarioDenuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UsuarioDenuncia.objects.count(), 0)

    # Error Testes

    def test_create_usuario_denuncia_error(self):
        client = APIClient()
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')

        data = {'comentario': 'Test 4', 'latitude': '1', 'longitude': '1', 'denuncia': str(denuncia.id)}
        request = client.post('/api/usuario_denuncia/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_usuario_denuncia_error(self):
        client = APIClient()
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')

        usuarioDenuncia = UsuarioDenuncia.objects.create(comentario='Test 5', latitude='1', longitude='1', denuncia=denuncia)
        usuarioDenuncia.save()
        data = {'comentario': 'Test Update', 'latitude': '1', 'longitude': '1', 'denuncia': str(denuncia.id)}
        request = client.put('/api/usuario_denuncia/'+str(usuarioDenuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_usuario_denuncia_error(self):
        client = APIClient()
        denuncia = Denuncia.objects.get(descricao='DenunciaTest')

        usuarioDenuncia = UsuarioDenuncia.objects.create(comentario='Test 6', latitude='1', longitude='1', denuncia=denuncia)
        usuarioDenuncia.save()
        request = client.delete('/api/usuario_denuncia/'+str(usuarioDenuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
