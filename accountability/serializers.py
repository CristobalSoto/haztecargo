from rest_framework import serializers
from .models import Deputy


class DeputySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deputy
        fields = ('__all__')