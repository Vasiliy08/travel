from django.contrib import admin
from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {'slug': ('name',)}
