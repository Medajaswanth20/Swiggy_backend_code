# swiggy_app/urls.py

from django.urls import path
from .views import milestone_view

urlpatterns = [
    path('', milestone_view, name='milestone'),
]
