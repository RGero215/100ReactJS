from rest_framework import serializers
from .models import Statistics, OnePLayer, TwoGames

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

class OnePLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnePLayer
        fields = '__all__'

class TwoGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoGames
        fields = '__all__'