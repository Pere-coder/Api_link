from rest_framework import serializers
from .models import Names


class NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = ['first_name', 'last_name']
        