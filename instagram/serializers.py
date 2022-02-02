from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = [
            'pk',
            'username',
            'message',
            'is_public',
            'created_at',
            'updated_at',
        ]