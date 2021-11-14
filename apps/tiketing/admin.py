from django.contrib import admin

from apps.tiketing.models import *

@admin.register(Tiket)
class TiketAdmin(admin.ModelAdmin):
    list_display = ["event","seat","user","status"]
