from rest_framework import serializers

from .models import Prefecture, InfectionStats, BehaviorStats


class InfectionDailyStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfectionStats
        fields = [
            'id',
            'new_infected',
            'current_infected',
            'total_infected',
            'total_recovered',
            'total_death',
            'restraint_ratio',
            'reported_date',
            'created_at',
            'updated_at',
        ]


class InfectionStatsSerializer(serializers.ModelSerializer):
    daily = InfectionDailyStatsSerializer(many=True, read_only=True)
    total_recovered = serializers.IntegerField()
    total_death = serializers.IntegerField()

    class Meta:
        model = Prefecture
        fields = ['name', 'name_en', 'total_recovered', 'total_death', 'daily']


class JapanInfectionStatsSerializer(serializers.Serializer):
    new_infected = serializers.IntegerField()
    current_infected = serializers.IntegerField()
    total_infected = serializers.IntegerField()
    total_recovered = serializers.IntegerField()
    total_death = serializers.IntegerField()
    reported_date = serializers.DateField()

    class Meta:
        fields = [
            'new_infected',
            'current_infected',
            'total_infected',
            'total_recovered',
            'total_death',
            'reported_date',
        ]


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
