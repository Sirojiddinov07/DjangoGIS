from django.db import models
from django.utils.translation import gettext_lazy as __

class Map(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = __("Map")
        verbose_name_plural = __("Maps")
