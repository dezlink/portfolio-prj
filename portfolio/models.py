from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    descriotion = models.CharField(max_length=250)
    image = models.ImageField9upload_to=('portfolio/images/')
    url = models.URLField(blank=True)

