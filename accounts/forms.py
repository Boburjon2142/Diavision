from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class UzbekAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Ism")
    last_name = forms.CharField(label="Familiya")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "phone",
            "birth_date",
            "gender",
            "region",
            "district",
            "height_cm",
            "weight_kg",
            "waist_cm",
            "emergency_contact",
            "preferred_language",
            "consent_ai_support",
        ]
        widgets = {"birth_date": forms.DateInput(attrs={"type": "date"})}
