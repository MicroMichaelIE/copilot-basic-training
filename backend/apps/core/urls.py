"""Core app URL Configuration."""
from django.urls import path
from apps.core.views import HelloWorldView

urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
]
