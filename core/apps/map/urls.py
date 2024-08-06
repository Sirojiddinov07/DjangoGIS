from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapViewSet, LocationViewSet, MediaViewSet

router = DefaultRouter()
router.register(r'maps', MapViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'media', MediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
