from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=100)
    clientImagePath = models.ImageField(upload_to = 'clientLogos/')

    def __str__(self):
        return self.clientName

class Andi(models.Model):
    andiName = models.CharField(max_length=150)
    andiPhotoPath = models.ImageField(upload_to = 'andis/')

    def __str__(self):
        return self.andiName

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length=100)
    projectDescription = models.TextField()

    def __str__(self):
        return self.projectTitle

class ProjectAndis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectAndi = models.ForeignKey(Andi, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.projectTitle + ": " + self.projectAndi.andiName

class ProjectImages(models.Model):
    position = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectImagePath = models.ImageField(upload_to = 'site_images/')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.project.projectTitle + ": " + self.projectImagePath.url

class ProjectTechnologyStacks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technologyName = models.CharField(max_length=100)
    technologyImagePath = models.ImageField(upload_to = 'tech_images/')
    important = models.BooleanField()

    class Meta:
        ordering = ['-important']
    
    def __str__(self):
        return self.project.projectTitle + ": " + self.technologyName
