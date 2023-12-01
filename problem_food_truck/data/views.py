from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckDataSerializer
from rest_framework import status

@api_view(['GET'])
def food_trucks_near_me(request):
    try:
        latitude = float(request.query_params.get('latitude'))
        longitude = float(request.query_params.get('longitude'))
        # find food trucks near location based on coordinates
        trucks_near_me = FoodTruck.objects.filter(
            latitude__range=(latitude - 0.01, latitude + 0.01),
            longitude__range=(longitude - 0.01, longitude + 0.01)
        )

        serializer = FoodTruckDataSerializer(trucks_near_me, many=True)
        return Response(serializer.data)
    except ValueError as e:
        error_message = "Invalid coordinates. Latitude and longitude must be numeric."
        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        error_message = "An error occurred while processing your request."
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
