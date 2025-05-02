"""Core app URL Configuration."""
from django.urls import path
from apps.core.views import CatListView

urlpatterns = [
    path('cats/', CatListView.as_view(), name='cat-list'),
]
