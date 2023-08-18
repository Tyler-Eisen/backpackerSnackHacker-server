from django.db import models
from .user import User
from .shop import Shop

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shops')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
