from django.contrib import admin

from .models import FoodQueryHistory


@admin.register(FoodQueryHistory)
class FoodQueryHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "meal_name", "label", "created_at")
