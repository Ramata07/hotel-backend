from django.shortcuts import render
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import viewsets, mixins, generics
# Create your views here.

# class HotelViewSet(viewsets.ViewSet): #crée les actions de la méthode HTTP
class HotelViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

