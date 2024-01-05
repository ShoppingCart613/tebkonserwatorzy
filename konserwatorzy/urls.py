from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:zadanie_id>/", views.zadanie, name="zadanie"),
    path("add_zadanie", views.add_zadanie, name="add_zadanie"),
]