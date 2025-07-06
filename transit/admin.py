from django.contrib import admin
from transit.models import Stop


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    pass