from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.apps.map.models import Map
from core.apps.map.serializers import MapSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [AllowAny]