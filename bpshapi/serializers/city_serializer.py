from rest_framework import serializers
from bpshapi.models import City

class CitySerializer(serializers.ModelSerializer):
    """JSON serializer for cities"""
    class Meta:
        model = City
        fields = ('id', 
                  'name',
                  'image_url',)
        depth = 1
