"""
URL configuration for homepage project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
]
