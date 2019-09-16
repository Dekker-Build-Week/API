from django.db import models

# Create your models here.
class Client(models.Model):
    clientName = models.CharField(max_length=100)
    imagePath = models.CharField(max_length=250)

    def __str__(self):
        return self.clientName