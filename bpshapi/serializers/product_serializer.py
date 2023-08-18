from rest_framework import serializers
from bpshapi.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Product
        fields = ( 'id',
                  'shop',
                  'user',
                  'name',
                  'price',
                  'image_url')
        # depth = 2
