# serializers.py

from rest_framework import serializers
from .models import Hospital  # Make sure Hospital model exists and is imported

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
