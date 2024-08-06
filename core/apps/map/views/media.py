from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.apps.map.models import Media
from core.apps.map.serializers import MediaSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [AllowAny]