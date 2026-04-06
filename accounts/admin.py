from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "gender", "region", "phone", "consent_ai_support")
    search_fields = ("user__username", "user__first_name", "user__last_name", "phone")
    list_filter = ("gender", "region", "consent_ai_support")
