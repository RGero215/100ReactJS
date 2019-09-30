from rest_framework import serializers
from .models import Test100React


class Test100ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test100React
        fields = '__all__'



