from django.contrib import admin
from core.apps.map.models import Map, Location, Media
from unfold.admin import ModelAdmin


@admin.register(Map)
class MapAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Media)
class MediasAdmin(ModelAdmin):
    list_display = ('id',  'media_type',)
