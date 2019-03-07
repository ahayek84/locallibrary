from django.shortcuts import render
from locallibrary.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import status

# Create your views here.