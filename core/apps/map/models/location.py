from django.db import models
from django.utils.translation import gettext_lazy as __

from core.apps.map.models import Map


class Location(models.Model):
    map = models.ForeignKey(Map, related_name='locations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __("Location")
        verbose_name_plural = __("Locations")
