from django.db import models

# Create your models here.
from rest_framework import serializers
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=10)