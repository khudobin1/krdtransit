from rest_framework import serializers
from .models import Stop


class StopSerializer(serializers.ModelSerializer):
    next_stops = serializers.PrimaryKeyRelatedField(many=True, queryset=Stop.objects.all())

    class Meta:
        model = Stop
        fields = ('id', 'name', 'latitude', 'longitude',  'transport_types', 'next_stops')