from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.data_access.user_repository import UserRepository


class UserTest(TestCase):
    def setUp(self):
        self.user_repository = UserRepository()
        self.usuario = {'username': 'teste', 'password': '123'}
        self.api_client = APIClient()
    
    def test_create_users(self):
        """
        POST - Cria um usuário
        """
        response = self.api_client.post(reverse('user-list'), self.usuario, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], self.user_repository.get(query_params={'id': response.data['id']}).id)