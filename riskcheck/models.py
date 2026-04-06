from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class RiskAssessment(TimeStampedModel):
    RISK_LEVELS = [("low", "Past"), ("medium", "O‘rta"), ("high", "Yuqori")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="risk_assessments")
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    height_cm = models.PositiveIntegerField()
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    waist_cm = models.PositiveIntegerField()
    food_habits = models.CharField(max_length=255)
    physical_activity = models.CharField(max_length=120)
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=1)
    stress_level = models.CharField(max_length=50)
    blood_pressure = models.CharField(max_length=20)
    blood_sugar = models.DecimalField(max_digits=5, decimal_places=2)
    family_history = models.BooleanField(default=False)
    smoking_status = models.CharField(max_length=50)
    alcohol_status = models.CharField(max_length=50)
    existing_conditions = models.CharField(max_length=255, blank=True)
    risk_level = models.CharField(max_length=20, choices=RISK_LEVELS)
    risk_percentage = models.PositiveIntegerField()
    ai_explanation = models.TextField()
    recommendations = models.TextField()
    next_steps = models.TextField()
    warning_text = models.TextField(blank=True)


class RiskFactorDetail(TimeStampedModel):
    assessment = models.ForeignKey(RiskAssessment, on_delete=models.CASCADE, related_name="risk_factors")
    factor_name = models.CharField(max_length=120)
    factor_score = models.PositiveIntegerField(default=0)
    factor_reason = models.TextField()
