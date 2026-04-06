from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.public_overview, name="public_overview"),
    path("list/", views.reading_list, name="list"),
    path("new/", views.reading_create, name="create"),
]
