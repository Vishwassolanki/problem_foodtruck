from django.urls import path
from .views import food_trucks_near_me

urlpatterns = [
    path('food-trucks-near-me/', food_trucks_near_me, name='food-trucks-near-me'),
]