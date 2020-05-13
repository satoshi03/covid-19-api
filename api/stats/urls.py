from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import JapanInfectionStatsViewSet, InfectionStatsViewSet, BehaviorStatsViewSet

router = DefaultRouter()
router.register(r'infection/prefectures', InfectionStatsViewSet, basename='InfectionStats')
router.register(r'infection/japan', JapanInfectionStatsViewSet, basename='JapanInfectionStats')
router.register(r'behavior', BehaviorStatsViewSet, basename='BehaviorStats')

urlpatterns = router.urls
