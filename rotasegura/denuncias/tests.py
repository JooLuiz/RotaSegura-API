from users.models import User
from denuncias.models import Denuncia
from tipo_denuncia.models import TipoDenuncia
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class DenunciaTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testes', password='123', email='testes@email.com', cpf='10907749402')
        user.save()
        tipoDenuncia = TipoDenuncia.objects.create(descricao='TipoDenunciaTest')
        tipoDenuncia.save()

    # Success Tests

    def test_create_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')
        client.force_authenticate(user=user)

        data = {'descricao': 'Test 1', 'tipo_denuncia': str(tipoDenuncia.id)}
        request = client.post('/api/denuncias/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Denuncia.objects.count(), 1)
        self.assertEqual(Denuncia.objects.get().descricao, 'Test 1')
    
    def test_update_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')
        client.force_authenticate(user=user)

        denuncia = Denuncia.objects.create(descricao='Test 2', tipo_denuncia=tipoDenuncia)
        denuncia.save()
        data = {'descricao': 'Test Update', 'tipo_denuncia': str(tipoDenuncia.id)}
        request = client.put('/api/denuncias/'+str(denuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Denuncia.objects.count(), 1)
        self.assertEqual(Denuncia.objects.get().descricao, 'Test Update')

    def test_delete_denuncia_done(self):
        client = APIClient()
        user = User.objects.get(username='testes')
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')
        client.force_authenticate(user=user)

        denuncia = Denuncia.objects.create(descricao='Test 3', tipo_denuncia=tipoDenuncia)
        denuncia.save()
        request = client.delete('/api/denuncias/'+str(denuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Denuncia.objects.count(), 0)

    # Error Testes

    def test_create_denuncia_error(self):
        client = APIClient()
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')

        data = {'descricao': 'Test 4', 'tipo_denuncia': str(tipoDenuncia.id)}
        request = client.post('/api/denuncias/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_denuncia_error(self):
        client = APIClient()
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')

        denuncia = Denuncia.objects.create(descricao='Test 5', tipo_denuncia=tipoDenuncia)
        denuncia.save()
        data = {'descricao': 'Test Update'}
        request = client.put('/api/denuncias/'+str(denuncia.id)+'/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_denuncia_error(self):
        client = APIClient()
        tipoDenuncia = TipoDenuncia.objects.get(descricao='TipoDenunciaTest')

        denuncia = Denuncia.objects.create(descricao='Test 6', tipo_denuncia=tipoDenuncia   )
        denuncia.save()
        request = client.delete('/api/denuncias/'+str(denuncia.id)+'/')
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
