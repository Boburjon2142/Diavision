from django.contrib import admin

from .models import RiskAssessment, RiskFactorDetail


class RiskFactorDetailInline(admin.TabularInline):
    model = RiskFactorDetail
    extra = 0


@admin.register(RiskAssessment)
class RiskAssessmentAdmin(admin.ModelAdmin):
    list_display = ("user", "risk_level", "risk_percentage", "blood_sugar", "created_at")
    list_filter = ("risk_level", "gender", "family_history")
    inlines = [RiskFactorDetailInline]
