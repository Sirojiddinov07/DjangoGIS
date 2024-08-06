from rest_framework import serializers

from core.apps.map.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'map', 'name', 'description', 'latitude', 'longitude', 'created_at', 'updated_at')
