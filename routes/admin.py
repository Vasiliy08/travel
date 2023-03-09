from django.contrib import admin

from routes.models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'travel_time', 'from_city', 'to_city')
    list_editable = ('travel_time',)