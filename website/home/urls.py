from django.contrib import admin  # noqa: F401
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="homepage")
]
