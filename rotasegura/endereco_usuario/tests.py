from django.contrib.auth.models import User
from endereco_usuario.models import EnderecoUsuario
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class EnderecoUsuarioTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testes', password='123', email='testes@email.com')
        user.save()

    # Success Tests

    def test_create_endereco_usuario_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        data = {'nome': 'Test 1', 'latitude': '1', 'longitude': '1'}
        request = client.post('/api/endereco_usuario/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EnderecoUsuario.objects.count(), 1)
        self.assertEqual(EnderecoUsuario.objects.get().nome, 'Test 1')
    
    def test_update_endereco_usuario_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        enderecoUsuario = EnderecoUsuario.objects.create(nome='Test 2', latitude='1', longitude='1')
        enderecoUsuario.save()

        data = {'nome': 'Test Update', 'latitude': '1', 'longitude': '1'}
        request = client.put('/api/endereco_usuario/'+str(enderecoUsuario.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(EnderecoUsuario.objects.count(), 1)
        self.assertEqual(EnderecoUsuario.objects.get().nome, 'Test Update')

    def test_delete_endereco_usuario_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        enderecoUsuario = EnderecoUsuario.objects.create(nome='Test 3', latitude='1', longitude='1')
        enderecoUsuario.save()
        request = client.delete('/api/endereco_usuario/'+str(enderecoUsuario.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EnderecoUsuario.objects.count(), 0)

    # Error Testes

    def test_create_endereco_usuario_error(self):
        client = APIClient()

        data = {'nome': 'Test 4', 'latitude': '1', 'longitude': '1'}
        request = client.post('/api/endereco_usuario/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_endereco_usuario_error(self):
        client = APIClient()

        enderecoUsuario = EnderecoUsuario.objects.create(nome='Test 5', latitude='1', longitude='1')
        enderecoUsuario.save()
        data = {'nome': 'Test Update', 'latitude': '1', 'longitude': '1'}
        request = client.put('/api/endereco_usuario/'+str(enderecoUsuario.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_endereco_usuario_error(self):
        client = APIClient()

        enderecoUsuario = EnderecoUsuario.objects.create(nome='Test 6', latitude='1', longitude='1')
        enderecoUsuario.save()
        request = client.delete('/api/endereco_usuario/'+str(enderecoUsuario.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
