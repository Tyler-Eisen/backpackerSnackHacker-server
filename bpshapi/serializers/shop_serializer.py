from rest_framework import serializers
from bpshapi.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    """JSON serializer for shops"""
    class Meta:
        model = Shop
        fields = ('id', 
                  'address', 
                  'image_url',
                  'name',
                  'city_id',
                  'favorited')
        depth = 2
        
