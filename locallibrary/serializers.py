from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)

    def create(self, validated_data):
        country_obj = Country(**validated_data)
        country_obj.save()
        return country_obj

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()
        return instance