from django.shortcuts import render

from .serializer import *
from rest_framework import viewsets, permissions

from .models import *

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


