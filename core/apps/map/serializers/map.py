from rest_framework import serializers

from core.apps.map.models import Map


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')