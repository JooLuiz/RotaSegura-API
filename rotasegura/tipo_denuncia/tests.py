from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from tipo_denuncia.models import TipoDenuncia

class TipoDenunciaTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testes', password='123', email='testes@email.com')
        user.save()

    # Success Tests

    def test_create_tipoDenuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        data = {'descricao': 'Test 1'}
        request = client.post('/api/tipodenuncia/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TipoDenuncia.objects.count(), 1)
        self.assertEqual(TipoDenuncia.objects.get().descricao, 'Test 1')
    
    def test_update_tipoDenuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        tipoDenuncia = TipoDenuncia.objects.create(descricao='Test 2')
        tipoDenuncia.save()
        data = {'descricao': 'Test Update'}
        request = client.put('/api/tipodenuncia/'+str(tipoDenuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(TipoDenuncia.objects.count(), 1)
        self.assertEqual(TipoDenuncia.objects.get().descricao, 'Test Update')

    def test_delete_tipoDenuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        client.force_authenticate(user=user)

        tipoDenuncia = TipoDenuncia.objects.create(descricao='Test 3')
        tipoDenuncia.save()
        request = client.delete('/api/tipodenuncia/'+str(tipoDenuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TipoDenuncia.objects.count(), 0)

    # Error Testes

    def test_create_tipoDenuncia_error(self):
        client = APIClient()

        data = {'descricao': 'Test 4'}
        request = client.post('/api/tipodenuncia/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_update_tipoDenuncia_error(self):
        client = APIClient()

        tipoDenuncia = TipoDenuncia.objects.create(descricao='Test 5')
        tipoDenuncia.save()
        data = {'descricao': 'Test Update'}
        request = client.put('/api/tipodenuncia/'+str(tipoDenuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tipoDenuncia_error(self):
        client = APIClient()

        tipoDenuncia = TipoDenuncia.objects.create(descricao='Test 6')
        tipoDenuncia.save()
        request = client.delete('/api/tipodenuncia/'+str(tipoDenuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
