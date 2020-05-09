from rest_framework import serializers

from .models import Prefecture, InfectionStats, BehaviorStats


class InfectionDailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectionStats
        fields = ['id', 'infected', 'recovered', 'reported_date']


class InfectionStatsSerializer(serializers.ModelSerializer):
    daily = InfectionDailyStatsSerializer(many=True, read_only=True)

    class Meta:
        model = Prefecture
        fields = ['name', 'daily']


class BehaviorDailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviorStats
        fields = ['id', 'restraint_ratio', 'reported_date']


class BehaviorStatsSerializer(serializers.ModelSerializer):
    daily = BehaviorDailyStatsSerializer(many=True, read_only=True)

    class Meta:
        model = Prefecture
        fields = ['name', 'daily']
