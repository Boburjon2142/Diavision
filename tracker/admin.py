from django.contrib import admin

from .models import SugarReading


@admin.register(SugarReading)
class SugarReadingAdmin(admin.ModelAdmin):
    list_display = ("user", "reading_type", "value", "measured_at", "is_unusual")
    list_filter = ("reading_type", "is_unusual")
