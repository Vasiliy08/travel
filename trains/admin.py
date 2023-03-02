from django.contrib import admin

from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'travel_time', 'from_city', 'to_city')
    list_editable = ('travel_time',)