from rest_framework import serializers
from bpshapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id',
                  'content', 
                  'product', 
                  'user')
