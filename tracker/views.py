from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import SugarReadingForm
from .models import SugarReading
from .services import get_tracker_summary


def public_overview(request):
    return render(request, "tracker/public_overview.html")


@login_required
def reading_list(request):
    readings = SugarReading.objects.filter(user=request.user)
    summary = get_tracker_summary(list(readings[:30]))
    return render(request, "tracker/reading_list.html", {"readings": readings[:20], "summary": summary})


@login_required
def reading_create(request):
    if request.method == "POST":
        form = SugarReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.is_unusual = reading.value < 4 or reading.value > 8.5
            reading.save()
            messages.success(request, "Qon shakari ko‘rsatkichi saqlandi.")
            return redirect("tracker:list")
    else:
        form = SugarReadingForm()
    return render(request, "tracker/reading_form.html", {"form": form})
