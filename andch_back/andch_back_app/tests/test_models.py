from django.test import TestCase
from andch_back_app.models import Client, Andi, Project

# Create your tests here.

class ClientModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')

    def test_clientname_max_length(self):
        client = Client.objects.get(clientName='British Airways')
        max_length = client._meta.get_field('clientName').max_length
        self.assertEquals(max_length, 100)
    
    def test_clientimagepath_max_length(self):
        client = Client.objects.get(clientName='British Airways')
        max_length = client._meta.get_field('clientImagePath').max_length
        self.assertEquals(max_length, 250)
    
    def test_object_name(self):
        client = Client.objects.get(clientName='British Airways')
        self.assertEquals(str(client), 'British Airways')
    
class AndiModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Andi.objects.create(andiName='John Smith', andiPhotoPath='127.0.0.1:8000/static/ba.png')
    
    def test_andiname_max_length(self):
        andi = Andi.objects.get(andiName='John Smith')
        max_length = andi._meta.get_field('andiName').max_length
        self.assertEquals(max_length, 150)
    
    def test_andiphotopath_max_length(self):
        andi = Andi.objects.get(andiName='John Smith')
        max_length = andi._meta.get_field('andiPhotoPath').max_length
        self.assertEquals(max_length, 250)
    
    def test_object_name(self):
        andi = Andi.objects.get(andiName='John Smith')
        self.assertEquals(str(andi), 'John Smith')

class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(projectTitle='British Airways Mobile App', projectDescription='test test test')
    
    def test_projecttitle_max_length(self):
        project = Project.objects.get(projectTitle='British Airways Mobile App')
        max_length = project._meta.get_field('projectTitle').max_length
        self.assertEquals(max_length, 100)

    def test_object_name(self):
        project = Project.objects.get(projectTitle='British Airways Mobile App')
        self.assertEquals(str(project), 'British Airways Mobile App')

