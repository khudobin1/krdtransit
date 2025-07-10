from rest_framework import serializers
from .models import Stop, Route, TransportType, Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    weekday_display = serializers.CharField(source="get_weekday_display", read_only=True)

    class Meta:
        model = Schedule
        fields = ("id", "stop", "route", "weekday", "weekday_display", "arrival_time")

class StopSerializer(serializers.ModelSerializer):
    next_stops = serializers.PrimaryKeyRelatedField(many=True, queryset=Stop.objects.all())
    routes = serializers.PrimaryKeyRelatedField(many=True, queryset=Route.objects.all())
    transport_types = serializers.SlugRelatedField(
        many=True,
        slug_field='code',
        queryset=TransportType.objects.all()
    )

    class Meta:
        model = Stop
        fields = ('id', 'name', 'latitude', 'longitude',  'transport_types', 'next_stops', 'routes')


class RouteSerializer(serializers.ModelSerializer):
    stops = serializers.PrimaryKeyRelatedField(
        queryset=Stop.objects.all(),
        many=True
    )
    transport_types = serializers.PrimaryKeyRelatedField(
        queryset=TransportType.objects.all()
    )

    class Meta:
        model = Route
        fields = ('id', 'number', 'name', 'transport_types', 'stops')
