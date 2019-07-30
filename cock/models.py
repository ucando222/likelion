from django.db import models

# Create your models here.
class Cock(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    component = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title