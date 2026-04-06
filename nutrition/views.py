from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import FoodAssistantForm
from .models import FoodQueryHistory
from .services import analyze_food


def assistant(request):
    result = None
    if request.method == "POST":
        form = FoodAssistantForm(request.POST)
        if form.is_valid():
            result = analyze_food(form.cleaned_data["meal_name"])
            if request.user.is_authenticated:
                FoodQueryHistory.objects.create(
                    user=request.user,
                    meal_name=form.cleaned_data["meal_name"],
                    label=result["label"],
                    portion_guidance=result["portion"],
                    alternatives=result["alternatives_text"],
                    ai_explanation=result["explanation"],
                )
            messages.success(request, "AI oziq-ovqat tahlili tayyor.")
    else:
        form = FoodAssistantForm()
    return render(request, "nutrition/assistant.html", {"form": form, "result": result})


@login_required
def history(request):
    items = FoodQueryHistory.objects.filter(user=request.user)
    return render(request, "nutrition/history.html", {"items": items})
