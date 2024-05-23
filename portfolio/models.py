from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(default='portfolio/images/', upload_to='portfolio/images/')
    url = models.URLField(blank=True)

