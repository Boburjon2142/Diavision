from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import UzbekAuthenticationForm, UserProfileForm, UserRegistrationForm
from .models import UserProfile


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = UzbekAuthenticationForm


class UserLogoutView(LogoutView):
    next_page = "pages:home"


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, "Profil muvaffaqiyatli yaratildi.")
            return redirect("dashboard:overview")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil ma’lumotlari yangilandi.")
            return redirect("accounts:profile")
    else:
        form = UserProfileForm(instance=profile)
    return render(request, "dashboard/profile.html", {"form": form, "profile": profile})
