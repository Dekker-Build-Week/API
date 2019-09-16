from django.db import models

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

    def __str__(self):
        return self.projectTitle

class ProjectAndis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectAndi = models.ForeignKey(Andi, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.projectTitle + ":" + self.projectAndi.andiName

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectImagePath = models.CharField(max_length=250)

    def __str__(self):
        return self.project.projectTitle + ":" + self.projectImagePath