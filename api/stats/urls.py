from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import InfectionStatsViewSet, BehaviorStatsViewSet

router = DefaultRouter()
router.register(r'infection', InfectionStatsViewSet, basename='InfectionStats')
router.register(r'behavior', BehaviorStatsViewSet, basename='BehaviorStats')

urlpatterns = router.urls
