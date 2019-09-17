from django.test import TestCase
from andch_back_app.models import Client, Andi, Project, ProjectAndis, ProjectImages, ProjectTechnologyStacks

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
        client = Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')
        Project.objects.create(client=client,projectTitle='British Airways Mobile App', projectDescription='test test test')
    
    def test_projecttitle_max_length(self):
        project = Project.objects.get(projectTitle='British Airways Mobile App')
        max_length = project._meta.get_field('projectTitle').max_length
        self.assertEquals(max_length, 100)

    def test_object_name(self):
        project = Project.objects.get(projectTitle='British Airways Mobile App')
        self.assertEquals(str(project), 'British Airways Mobile App')

class ProjectAndisModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')
        project = Project.objects.create(client=client, projectTitle='British Airways Mobile App', projectDescription='test test test')
        andi = Andi.objects.create(andiName='John Smith', andiPhotoPath='127.0.0.1:8000/static/ba.png')
        ProjectAndis.objects.create(project=project, projectAndi=andi)
    
    def test_object_name(self):
        projectAndis = ProjectAndis.objects.get(project=Project.objects.get(projectTitle='British Airways Mobile App'))
        self.assertEqual(str(projectAndis), 'British Airways Mobile App: John Smith')

class ProjectImagesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')
        project = Project.objects.create(client=client, projectTitle='British Airways Mobile App', projectDescription='test test test')
        ProjectImages.objects.create(project=project, projectImagePath='127.0.0.1:8000/static/ba.png', position=1)
        ProjectImages.objects.create(project=project, projectImagePath='127.0.0.1:8000/static/ba.png', position=0)
        ProjectImages.objects.create(project=project, projectImagePath='127.0.0.1:8000/static/ba.png', position=2)

    def test_position_ordering_correct(self):
        projects = ProjectImages.objects.filter(project=Project.objects.get(projectTitle='British Airways Mobile App'))
        self.assertEqual(1, projects[1].position)

    def test_object_name(self):
        projectImages = ProjectImages.objects.get(project=Project.objects.get(projectTitle='British Airways Mobile App'), position=0)
        self.assertEqual(str(projectImages), 'British Airways Mobile App: 127.0.0.1:8000/static/ba.png')
    
class ProjectTechnologyStacksTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')
        project = Project.objects.create(client=client, projectTitle='British Airways Mobile App', projectDescription='test test test')
        ProjectTechnologyStacks.objects.create(project=project, important=False, technologyName='Java', technologyImagePath='test')
        ProjectTechnologyStacks.objects.create(project=project, important=True, technologyName='Java', technologyImagePath='test')
    
    def test_important_ordering_correct(self):
        projectStack = ProjectTechnologyStacks.objects.filter(project=Project.objects.get(projectTitle='British Airways Mobile App'))
        self.assertEquals(True, projectStack[0].important)
    
    def test_object_name(self):
        projectStack = ProjectTechnologyStacks.objects.get(project=Project.objects.get(projectTitle='British Airways Mobile App'), important=True)
        self.assertEqual(str(projectStack), 'British Airways Mobile App: Java')