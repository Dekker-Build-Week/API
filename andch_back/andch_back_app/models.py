from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=100)
    clientImagePath = models.ImageField(upload_to = 'clientLogos/', help_text='Please ensure that any client logos include the company"s name in the logo')

    class Meta:
        verbose_name = 'Client'

    def __str__(self):
        return self.clientName

class Andi(models.Model):
    andiName = models.CharField(max_length=150)
    andiPhotoPath = models.ImageField(upload_to = 'andis/')

    class Meta:
        verbose_name = 'ANDi'

    def __str__(self):
        return self.andiName

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    projectTitle = models.CharField(max_length=100)
    projectDescription = models.TextField()

    class Meta:
        verbose_name = 'Project'

    def __str__(self):
        return self.projectTitle

class ProjectAndis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectAndi = models.ForeignKey(Andi, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Project ANDi'
        verbose_name_plural = 'Project ANDis'

    def __str__(self):
        return self.project.projectTitle + ": " + self.projectAndi.andiName

class ProjectImages(models.Model):
    position = models.IntegerField(help_text='Please enter a value of 0 for the cover image that will appear on the home page')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectImagePath = models.ImageField(upload_to = 'site_images/')

    class Meta:
        ordering = ['position']
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

    def __str__(self):
        return self.project.projectTitle + ": " + self.projectImagePath.url

class ProjectTechnologyStacks(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technologyName = models.CharField(max_length=100)
    technologyImagePath = models.ImageField(upload_to = 'tech_images/')
    important = models.BooleanField(help_text='By ticking this value, the logo of the technology will appear on the home page')

    class Meta:
        ordering = ['-important']
        verbose_name = 'Project Technology Stack'
        verbose_name_plural = 'Project Technology Stacks'
    
    def __str__(self):
        return self.project.projectTitle + ": " + self.technologyName

class ProjectVideos(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    projectVideoPath = models.FileField(upload_to = 'project_videos/')

    class Meta:
        verbose_name = 'Project Video'
        verbose_name_plural = 'Project Videos'

    def __str__(self):
        return self.project.projectTitle + ": " + self.projectVideoPath.url
