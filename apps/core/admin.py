from django.contrib import admin
# from jsonfield import JSONField

from apps.core.models import *

@admin.register(Stadiom)
class StadiomAdmin(admin.ModelAdmin):
    list_display = ["fa_title","en_title","capacity"]

@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    list_display = ["stadiom","enable"]
    list_filter = ["enable",]


@admin.register(SeatMapDetail)
class SeatMapDetailAdmin(admin.ModelAdmin):
    list_display = ["seat_name","layout","enable"]
    list_filter = ["enable","layout",]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["host_team","guest_team","event_date"]
    list_filter = ["stadiom",]
