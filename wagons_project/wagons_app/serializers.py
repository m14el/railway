from rest_framework import serializers
from .models import Wagon


class WagonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wagon
        fields = '__all__'