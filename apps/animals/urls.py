from django.contrib import admin
from django.urls import path
from apps.animals.apis import AnimalsList, AnimalAdoptionRequestHandler


urlpatterns = [
    path('animals/', AnimalsList.as_view(), name='animals'),
    path('adoption-requests/', AnimalAdoptionRequestHandler.as_view(), name='adoption_request'),
    path('adoption-requests/<int:id>/', AnimalAdoptionRequestHandler.as_view(), name='adoption_request_specific'),
]