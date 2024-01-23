from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'port/images/')
    url = models.URLField(blank = True) # blank = True because not necessary will have an URL