from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Avg, Sum, Prefetch

from .serializers import InfectionStatsSerializer, BehaviorStatsSerializer
from .models import InfectionStats, BehaviorStats, Prefecture


class BaseStatsViewSet(viewsets.ViewSet):
    def get_queryset(self):
        qs = self.queryset

        # filtering date if it is included in request param
        start_date = self.request.query_params.get('start_date')
        if start_date:
            qs = qs.filter(reported_date__gte=start_date)
        end_date = self.request.query_params.get('end_date')
        if end_date:
            qs = qs.filter(reported_date__lt=end_date)

        # filtering prefecture if it is included in request param
        pref_qs = Prefecture.objects.all()
        prefecture = self.request.query_params.get('prefecture')
        if prefecture:
            pref_qs = pref_qs.filter(name=prefecture)

        # fetch stats
        return pref_qs.prefetch_related(Prefetch("basestats_set", queryset=qs.order_by('reported_date')))


class InfectionStatsViewSet(BaseStatsViewSet):
    queryset = InfectionStats.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = []
        for q in queryset:
            total = q.basestats_set.all().aggregate(
                total_infected=Sum('infected'),
                total_recovered=Sum('recovered'),
                total_death=Sum('death'),
            )
            dic = {
                'name': q.name,
                'daily': q.basestats_set.all()
            }
            dic.update(total)
            data.append(dic)
        serializer = InfectionStatsSerializer(data, many=True)
        return Response(serializer.data)


class BehaviorStatsViewSet(BaseStatsViewSet):
    queryset = BehaviorStats.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        data = []
        for q in queryset:
            avg = q.basestats_set.all().aggregate(
                average_restraint_ratio=Avg('restraint_ratio'),
            )
            dic = {
                'name': q.name,
                'daily': q.basestats_set.all()
            }
            dic.update(avg)
            data.append(dic)
        serializer = BehaviorStatsSerializer(data, many=True)
        return Response(serializer.data)
