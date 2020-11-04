from django.contrib import admin

from locations.models import *


@admin.register(Titul)
class TitulAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number']
