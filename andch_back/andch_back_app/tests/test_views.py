from django.test import TestCase
from andch_back_app.models import Client
import json

class AllClientsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(clientName='British Airways', imagePath='a/b/c')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/andch_back_app/clients/')
        self.assertEqual(response.status_code, 200)

    def test_view_one_client_data_setup_correctly(self):
        response = json.loads(self.client.get('/andch_back_app/clients/').content)
        self.assertEqual(str(response), '{\'clients\': [{\'clientName\': \'British Airways\', \'imagePath\': \'a/b/c\'}]}')
    
    def test_view_no_data(self):
        Client.objects.all().delete()
        response = json.loads(self.client.get('/andch_back_app/clients/').content)
        self.assertEqual(str(response), '{\'clients\': []}')
    
    def test_view_multiple_clients_data_setup_correctly(self):
        Client.objects.create(clientName='Lloyds Bank', imagePath='e/d/f')
        response = json.loads(self.client.get('/andch_back_app/clients/').content)
        self.assertEqual(str(response), '{\'clients\': [{\'clientName\': \'British Airways\', \'imagePath\': \'a/b/c\'}, {\'clientName\': \'Lloyds Bank\', \'imagePath\': \'e/d/f\'}]}')