from django.db import models
from .city import City

class Shop(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='shops')
    
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1000, default="")
    
