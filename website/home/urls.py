from django.contrib import admin  # noqa: F401
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("about-us", views.aboutus, name="aboutus"),
    path("projects", views.projects, name="projects"),
    path("courses", views.courses, name="courses"),
    path("contactus", views.contactus, name="contactus"),
    path("blog", views.blog, name="blog"),
    path("login", views.login, name="login"),
    path("registration", views.registration, name="registration"),
]
