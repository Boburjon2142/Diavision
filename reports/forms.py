from django import forms


class ReportFilterForm(forms.Form):
    report_type = forms.ChoiceField(
        label="Hisobot turi",
        choices=[("weekly", "Haftalik"), ("monthly", "Oylik")],
        required=False,
    )
