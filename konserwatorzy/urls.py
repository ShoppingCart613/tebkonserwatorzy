from django.urls import path
from . import views
from django.contrib.auth import views as login

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:zadanie_id>/", views.zadanie, name="zadanie"),
    path("add_zadanie/", views.add_zadanie, name="add_zadanie"),
    path("login/", login.LoginView.as_view(), name="login"),
]