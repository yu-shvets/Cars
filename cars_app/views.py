from django.shortcuts import render
from rest_framework import generics
from .models import Cars
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CarList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('manufacturer', 'model', 'age')


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
