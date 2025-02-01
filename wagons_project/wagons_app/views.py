from django.shortcuts import render

from rest_framework import generics
from .models import Wagon
from .serializers import WagonSerializer


class WagonListCreateView(generics.ListCreateAPIView):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer


class WagonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wagon.objects.all()
    serializer_class = WagonSerializer