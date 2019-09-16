from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=100)
    clientImagePath = models.CharField(max_length=250)

    def __str__(self):
        return self.clientName

class Andi(models.Model):
    andiName = models.CharField(max_length=150)
    andiPhotoPath = models.CharField(max_length=250)

    def __str__(self):
        return self.andiName

class Project(models.Model):
    projectTitle = models.CharField(max_length=100)
    projectDescription = models.TextField()
    projectImages = ListTextField(base_field=models.CharField(max_length=200))

    def __str__(self):
        return self.projectTitle

class ProjectAndis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    andi = models.ForeignKey(Andi, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + ":" + self.andi.name