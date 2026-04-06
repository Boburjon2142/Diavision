from django.urls import path

from . import views

app_name = "nutrition"

urlpatterns = [
    path("", views.assistant, name="assistant"),
    path("history/", views.history, name="history"),
]
