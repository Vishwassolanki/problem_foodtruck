from rest_framework import serializers
from .models import FoodTruck

class FoodTruckDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = ['locationId', 'applicant', 'latitude', 'longitude','address']