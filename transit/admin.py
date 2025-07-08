from django.contrib import admin
from transit.models import Stop, Route


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name', 'transport_types')
    readonly_fields = ('show_routes',)

    def show_routes(self, obj):
        return ", ".join(str(r.id) for r in obj.routes.all())
    show_routes.short_description = ("Маршруты")


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('transport_types', 'number', 'name')