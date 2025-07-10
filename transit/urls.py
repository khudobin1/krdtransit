from django.urls import include, path
from rest_framework import routers

from transit.views import RouteViewSet, StopViewSet, ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'stops', StopViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]