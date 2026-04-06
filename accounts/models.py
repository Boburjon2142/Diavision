from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class UserProfile(TimeStampedModel):
    GENDER_CHOICES = [
        ("female", "Ayol"),
        ("male", "Erkak"),
        ("other", "Boshqa"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    region = models.CharField(max_length=120, blank=True)
    district = models.CharField(max_length=120, blank=True)
    height_cm = models.PositiveIntegerField(default=170)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, default=70)
    waist_cm = models.PositiveIntegerField(default=90)
    emergency_contact = models.CharField(max_length=120, blank=True)
    preferred_language = models.CharField(max_length=20, default="uz")
    consent_ai_support = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_username()} profili"
