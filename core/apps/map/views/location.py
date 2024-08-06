from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.apps.map.models import Location
from core.apps.map.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]