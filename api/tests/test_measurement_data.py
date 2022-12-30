from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.data_access.measurement_data_repository import MeasurementDataRepository
from api.data_access.duplicate_measurement_data_repository import DuplicateMeasurementDataRepository


class MeasurementDataTest(TestCase):
    def setUp(self):
        self.measurement_data_repository = MeasurementDataRepository()
        self.duplicate_measurement_data_repository = DuplicateMeasurementDataRepository()
        self.usuario = {'username': 'teste', 'password': '123'}
        self.api_client = APIClient()

        self.api_client.post(reverse('user-list'), self.usuario)
        response = self.api_client.post(reverse('login'), self.usuario, format='json')
        self.api_client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])

        self.measurement_data = {'sensor_id': 7, 'measured_at': "2022-12-12 11:25:00", 'value': 147}

    def test_list_measurement_data(self):
        """
        GET - Lista os dados de medição armazenados e os duplicados.
        """
        response = self.api_client.get(reverse('measurement-list'), {'value': 5, 'time': 'hour'}, format='json')

        # Verifico:
        # Se o status é 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_with_not_authentication(self):
        """
        GET - Lista os dados de medição armazenados e os duplicados.
        """
        self.api_client.credentials(HTTP_AUTHORIZATION='Token')
        response = self.api_client.get(reverse('measurement-list'), {'value': 5, 'time': 'hour'}, format='json')

        # Verifico:
        # Se o status é 401
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_without_query_params(self):
        """
        GET - Realiza uma requisição com a ausência de um ou mais query params.
        """
        response_wrong_value = self.api_client.get(reverse('measurement-list'), {'wrong-value': 5, 'time': 'hour'}, format='json')
        response_wrong_time = self.api_client.get(reverse('measurement-list'), {'value': 5, 'wrong-time': 'hour'}, format='json')
        response_without_query_params = self.api_client.get(reverse('measurement-list'), format='json')

        self.assertEqual(response_wrong_value.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_wrong_time.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_without_query_params.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_wrong_query_params(self):
        """
        GET - Realiza uma requisição com query params incorretos.
        """
        response_value_not_allowed = self.api_client.get(reverse('measurement-list'), {'value': 80, 'time': 'hour'}, format='json')
        response_negative_value = self.api_client.get(reverse('measurement-list'), {'value': -80, 'time': 'hour'}, format='json')
        response_time_not_allowed = self.api_client.get(reverse('measurement-list'), {'value': 5, 'time': 'test'}, format='json')

        self.assertEqual(response_value_not_allowed.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response_negative_value.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_time_not_allowed.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_methods_not_allowed(self):
        """
        Testa métodos não permitidos como PUT, PATCH e DELETE.
        """
        response_put = self.api_client.put(reverse('measurement-list'), self.measurement_data, format='json')
        response_patch = self.api_client.patch(reverse('measurement-list'), self.measurement_data, format='json')
        response_delete = self.api_client.delete(reverse('measurement-list'), format='json')

        # Verifico:
        # - Se o status de todas as responses é 405
        self.assertEqual(response_put.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response_patch.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response_delete.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)