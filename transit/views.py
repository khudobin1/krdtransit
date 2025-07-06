from django.shortcuts import render
from rest_framework import viewsets

from transit.models import Stop
from transit.serializers import StopSerializer


class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer