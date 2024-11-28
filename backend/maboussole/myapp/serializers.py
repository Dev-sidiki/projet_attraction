from rest_framework import serializers
from .models import MyApp

class MyAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApp
        fields = '__all__'
