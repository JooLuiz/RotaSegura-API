from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class AccountTests(APITestCase):
    def test_create_user(self):
        client = APIClient()
        userData = {'username': 'testes', 'password': '123', 'email': 'testes@email.com'}
        request = client.post('/api/auth/register', userData, format='json')
        
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testes')
