from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class HealthReport(TimeStampedModel):
    REPORT_TYPES = [("weekly", "Haftalik"), ("monthly", "Oylik")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="health_reports")
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    average_sugar = models.DecimalField(max_digits=5, decimal_places=2)
    trend_direction = models.CharField(max_length=50)
    adherence_score = models.PositiveIntegerField(default=0)
    risk_trend = models.CharField(max_length=120)
    executive_summary = models.TextField()
    ai_recommendation = models.TextField()


class AlertLog(TimeStampedModel):
    LEVELS = [("info", "Info"), ("warning", "Ogohlantirish"), ("critical", "Kritik")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="alert_logs")
    title = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=LEVELS)
    message = models.TextField()
    resolved = models.BooleanField(default=False)


class AIInsightLog(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ai_insights")
    module = models.CharField(max_length=120)
    summary = models.CharField(max_length=255)
    detail = models.TextField()


class LifestyleScoreSnapshot(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lifestyle_scores")
    score = models.PositiveIntegerField()
    activity_score = models.PositiveIntegerField(default=0)
    nutrition_score = models.PositiveIntegerField(default=0)
    sleep_score = models.PositiveIntegerField(default=0)
    stress_score = models.PositiveIntegerField(default=0)
