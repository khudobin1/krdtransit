from rest_framework import serializers
from .models import Stop, Route


class StopSerializer(serializers.ModelSerializer):
    next_stops = serializers.PrimaryKeyRelatedField(many=True, queryset=Stop.objects.all())
    routes = serializers.PrimaryKeyRelatedField(many=True, queryset=Route.objects.all())

    class Meta:
        model = Stop
        fields = ('id', 'name', 'latitude', 'longitude',  'transport_types', 'next_stops', 'routes')


class RouteSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'number', 'name', 'stops')