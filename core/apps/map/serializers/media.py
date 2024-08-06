from rest_framework import serializers

from core.apps.map.models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'location', 'media_type', 'file_url', 'created_at', 'updated_at')