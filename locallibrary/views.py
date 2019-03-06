from django.shortcuts import render
from locallibrary.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def add_county(request):
    country_serializer = CountrySerializer(data=request.data)
    if country_serializer.is_valid():
        country_serializer.save()
        return Response({"data": "Country added successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in country_serializer.errors.keys():
            error_details.append({"field": key, "message": country_serializer.errors[key][0]})

        data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return 'hahahaha';