from rest_framework import serializers

from .models import InfectionStats


class InfectionStatsSerializer(serializers.ModelSerializer):
    prefecture = serializers.StringRelatedField(many=False)

    class Meta:
        model = InfectionStats
        fields = '__all__'
