from django.contrib import admin

from .models import AIInsightLog, AlertLog, HealthReport, LifestyleScoreSnapshot


admin.site.register(HealthReport)
admin.site.register(AlertLog)
admin.site.register(AIInsightLog)
admin.site.register(LifestyleScoreSnapshot)
