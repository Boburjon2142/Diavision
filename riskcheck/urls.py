from django.urls import path

from . import views

app_name = "riskcheck"

urlpatterns = [
    path("", views.public_check, name="public_check"),
    path("new/", views.assessment_create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]
