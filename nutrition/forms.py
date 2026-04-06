from django import forms


class FoodAssistantForm(forms.Form):
    meal_name = forms.CharField(label="Taom nomi")
