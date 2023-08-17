from rest_framework import serializers
from bpshapi.models import User

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = User
        fields = ('id', 
                  'uid', 
                  'name',
                  'country_of_origin',  
                  'image_url', )
        depth = 2
