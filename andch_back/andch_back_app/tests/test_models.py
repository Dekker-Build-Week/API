from django.test import TestCase
from andch_back_app.models import Client

# Create your tests here.

class ClientModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(clientName='British Airways', imagePath='127.0.0.1:8000/static/ba.png')

    def test_clientname_max_length(self):
        client = Client.objects.get(clientName='British Airways')
        max_length = client._meta.get_field('clientName').max_length
        self.assertEquals(max_length, 100)
    
    def test_imagepath_max_length(self):
        client = Client.objects.get(clientName='British Airways')
        max_length = client._meta.get_field('imagePath').max_length
        self.assertEquals(max_length, 250)
    
    def test_object_name(self):
        client = Client.objects.get(clientName='British Airways')
        self.assertEquals(str(client), 'British Airways')

