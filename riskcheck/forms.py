from django import forms

from .models import RiskAssessment


class RiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = RiskAssessment
        exclude = ["user", "bmi", "risk_level", "risk_percentage", "ai_explanation", "recommendations", "next_steps", "warning_text"]

    def clean(self):
        cleaned = super().clean()
        height_cm = cleaned.get("height_cm")
        weight_kg = cleaned.get("weight_kg")
        if height_cm and weight_kg:
            bmi = float(weight_kg) / ((height_cm / 100) ** 2)
            cleaned["bmi"] = round(bmi, 2)
        return cleaned
