from django.db import models

class City(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1000)
