from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InfectionStatsViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'infection', InfectionStatsViewSet, basename='InfectionStats')

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
