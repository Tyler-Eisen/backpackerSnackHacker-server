from django.db import models
from .user import User
from .product import Product

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    
    content = models.CharField(max_length=255)
