from django.contrib import admin
from transit.models import Stop, Route, TransportType


@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('show_routes',)

    def show_transport_types(self, obj):
        return ", ".join(t.name for t in obj.transport_types.all())

    show_transport_types.short_description = "Типы транспорта"

    def show_routes(self, obj):
        return ", ".join(str(r.id) for r in obj.routes.all())
    show_routes.short_description = ("Маршруты")


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('transport_types', 'number', 'name')


@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    pass