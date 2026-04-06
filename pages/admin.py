from django.contrib import admin

from .models import Article, DoctorRequest, FAQ


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "featured", "is_published", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "featured", "is_published")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "display_order", "is_active")
    list_editable = ("display_order", "is_active")


@admin.register(DoctorRequest)
class DoctorRequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "region", "status", "created_at")
    list_filter = ("status", "region")
