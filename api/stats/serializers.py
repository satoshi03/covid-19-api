from rest_framework import serializers

from .models import Prefecture, InfectionStats, BehaviorStats


class InfectionDailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectionStats
        fields = ['id', 'infected', 'recovered', 'reported_date']


class InfectionStatsSerializer(serializers.ModelSerializer):
    daily = InfectionDailyStatsSerializer(many=True, read_only=True)
    total_infected = serializers.IntegerField()
    total_recovered = serializers.IntegerField()
    total_death = serializers.IntegerField()

    class Meta:
        model = Prefecture
        fields = ['name', 'total_infected', 'total_recovered', 'total_death', 'daily']


class BehaviorDailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviorStats
        fields = ['id', 'restraint_ratio', 'reported_date']


class BehaviorStatsSerializer(serializers.ModelSerializer):
    daily = BehaviorDailyStatsSerializer(many=True, read_only=True)
    average_restraint_ratio = serializers.FloatField()

    class Meta:
        model = Prefecture
        fields = ['name', 'average_restraint_ratio', 'daily']
