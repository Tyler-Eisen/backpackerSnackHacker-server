from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    
    country_of_origin = models.CharField(max_length=255)
    
    uid = models.CharField(max_length=255, unique=True)
    
    image_url = models.CharField(max_length=1000, default=1)
