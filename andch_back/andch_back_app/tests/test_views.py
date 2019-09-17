from django.test import TestCase
from andch_back_app.models import Client, Project, Andi, ProjectAndis, ProjectImages, ProjectTechnologyStacks
import json
from andch_back_app.tests.assertions import assert_valid_schema


class AllClientsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Client.objects.create(clientName='British Airways', clientImagePath='a/b/c')

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
        Client.objects.create(clientName='Lloyds Bank', clientImagePath='e/d/f')
        response = json.loads(self.client.get('/andch_back_app/clients/').content)
        self.assertEqual(str(response), '{\'clients\': [{\'clientName\': \'British Airways\', \'imagePath\': \'a/b/c\'}, {\'clientName\': \'Lloyds Bank\', \'imagePath\': \'e/d/f\'}]}')


class AllProjectsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(clientName='British Airways', clientImagePath='127.0.0.1:8000/static/ba.png')
        andi = Andi.objects.create(andiName='John Smith', andiPhotoPath='127.0.0.1:8000/static/ba.png')
        project = Project.objects.create(client=client, projectTitle='British Airways Mobile App', projectDescription='test test test')

        ProjectImages.objects.create(project=project, projectImagePath='127.0.0.1:8000/static/ba.png', position=1)
        ProjectAndis.objects.create(project=project, projectAndi=andi)
        ProjectTechnologyStacks.objects.create(project=project, important=False, technologyName='Java', technologyImagePath='test')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/andch_back_app/projects/')
        self.assertEqual(response.status_code, 200)

    def test_all_projects_response_schema(self):
        response = json.loads(self.client.get('/andch_back_app/projects/').content)
        assert_valid_schema(response, 'projectSchema.json')