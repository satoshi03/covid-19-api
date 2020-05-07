from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import InfectionStatsSerializer
from .models import InfectionStats


class InfectionStatsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = InfectionStats.objects.all()
        serializer = InfectionStatsSerializer(queryset, many=True)
        return Response(serializer.data)
