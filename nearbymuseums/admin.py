from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Museum
# Register your models here.

@admin.register(Museum)
class MuseumAdmin(OSMGeoAdmin):
    list_display = ("name", "location")
