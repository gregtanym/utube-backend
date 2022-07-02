from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    thumbnail = serializers.ImageField()
    class Meta:
        model = Video
        fields = ('id', 'file', 'title', 'thumbnail', 'views', 'description', 'category', 'create_at')