from django.urls import path

from calculations import views

urlpatterns = [
    path("difference", views.difference, name="difference"),
]
