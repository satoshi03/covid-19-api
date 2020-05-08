from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import InfectionStatsSerializer, BehaviorStatsSerializer
from .models import InfectionStats, BehaviorStats


class BaseStatsViewSet(viewsets.ViewSet):
    def get_queryset(self):
        queryset = BehaviorStats.objects.all()
        start_date = self.request.query_params.get('start_date')
        if start_date:
            queryset = queryset.filter(reported_date__gte=start_date)

        end_date = self.request.query_params.get('end_date')
        if end_date:
            queryset = queryset.filter(reported_date__lt=end_date)

        prefecture = self.request.query_params.get('prefecture')
        if prefecture:
            queryset = queryset.filter(prefecture__name=prefecture)
        return queryset


class InfectionStatsViewSet(BaseStatsViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = InfectionStatsSerializer(queryset, many=True)
        return Response(serializer.data)


class BehaviorStatsViewSet(BaseStatsViewSet):
    def list(self, request):
        queryset = self.get_queryset()
        serializer = BehaviorStatsSerializer(queryset, many=True)
        return Response(serializer.data)
