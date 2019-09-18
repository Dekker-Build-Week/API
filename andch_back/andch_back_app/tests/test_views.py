from django.test import TestCase
from andch_back_app.models import Client, Project, Andi, ProjectAndis, ProjectImages, ProjectTechnologyStacks
import json
from andch_back_app.tests.assertions import assert_valid_schema
import tempfile


class AllProjectsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        client = Client.objects.create(clientName='British Airways', clientImagePath=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        andi = Andi.objects.create(andiName='John Smith', andiPhotoPath=tempfile.NamedTemporaryFile(suffix=".jpg").name)
        project = Project.objects.create(client=client, projectTitle='British Airways Mobile App', projectDescription='test test test')

        ProjectImages.objects.create(project=project, projectImagePath=tempfile.NamedTemporaryFile(suffix=".jpg").name, position=1)
        ProjectAndis.objects.create(project=project, projectAndi=andi)
        ProjectTechnologyStacks.objects.create(project=project, important=False, technologyName='Java', technologyImagePath=tempfile.NamedTemporaryFile(suffix=".jpg").name)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/andch_back_app/projects/')
        self.assertEqual(response.status_code, 200)

    def test_all_projects_response_schema(self):
        response = json.loads(self.client.get('/andch_back_app/projects/').content)
        assert_valid_schema(response, 'projectSchema.json')
