from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class AccountTests(APITestCase):
    def test_create_user(self):
        client = APIClient()
        userData = {'username': 'testes', 'password': '123', 'email': 'testes@email.com', 'cpf': '10907749402'}
        request = client.post('/api/auth/register', userData, format='json')
        
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testes')
