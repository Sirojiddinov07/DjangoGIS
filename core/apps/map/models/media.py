from django.db import models
from django.utils.translation import gettext_lazy as __

from core.apps.map.models import Location


class Media(models.Model):
    location = models.ForeignKey(Location, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=50)
    file_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.media_type

    class Meta:
        verbose_name = __("Media")
        verbose_name_plural = __("Medias")
