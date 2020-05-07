from rest_framework import serializers

from .models import InfectionStats, BehaviorStats


class InfectionStatsSerializer(serializers.ModelSerializer):
    prefecture = serializers.StringRelatedField(many=False)

    class Meta:
        model = InfectionStats
        fields = '__all__'


class BehaviorStatsSerializer(serializers.ModelSerializer):
    prefecture = serializers.StringRelatedField(many=False)

    class Meta:
        model = BehaviorStats
        fields = '__all__'
