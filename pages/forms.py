from django import forms

from .models import DoctorRequest


class ContactForm(forms.Form):
    full_name = forms.CharField(label="F.I.Sh.")
    phone = forms.CharField(label="Telefon")
    message = forms.CharField(label="Xabar", widget=forms.Textarea)


class DoctorRequestForm(forms.ModelForm):
    class Meta:
        model = DoctorRequest
        fields = ["full_name", "phone", "region", "note"]
        labels = {
            "full_name": "F.I.Sh.",
            "phone": "Telefon",
            "region": "Hudud",
            "note": "Qo‘shimcha izoh",
        }
