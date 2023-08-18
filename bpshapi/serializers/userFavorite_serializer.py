from rest_framework import serializers
from bpshapi.models import UserFavorite

class UserFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorite
        fields = ['user', 'shop']
