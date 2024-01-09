from django.urls import path
from . import views
from django.contrib.auth import views as login

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:zadanie_id>/", views.zadanie, name="zadanie"),
    path("add_zadanie/", views.add_zadanie, name="add_zadanie"),
    path("<int:zadanie_id>/edit", views.edit, name="edit"),
    path("login/", login.LoginView.as_view(), name="login"),
    path('logout/', views.logout, name='logout'),
]