from django.shortcuts import render
from rest_framework import viewsets

from transit.models import Stop, Route, Schedule
from transit.serializers import StopSerializer, RouteSerializer, ScheduleSerializer


class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer