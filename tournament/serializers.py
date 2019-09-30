from rest_framework import serializers
from .models import Four, FourPomodoro

class FourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Four
        fields = '__all__'

class FourPomodoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourPomodoro
        fields = '__all__'