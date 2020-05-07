from rest_framework import serializers

from .models import DailyStats


class DailyStatsSerializer(serializers.ModelSerializer):
    prefecture = serializers.StringRelatedField(many=False)

    class Meta:
        model = DailyStats
        #fields = ['prefecture', 'patients', 'deaths']
        fields = '__all__'

