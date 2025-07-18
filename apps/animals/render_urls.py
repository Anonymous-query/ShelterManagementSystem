from django.contrib import admin
from django.urls import path
from apps.animals.views import animal_view


urlpatterns = [
    path('animals/dashboard', animal_view, name='animals_view'),
]