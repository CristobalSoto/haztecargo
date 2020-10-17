from django.shortcuts import render
from rest_framework import generics
from .models import Deputy
from .serializers import DeputySerializer
# Create your views here.

class DeputyListCreate(generics.ListCreateAPIView):
    queryset = Deputy.objects.all()
    serializer_class = DeputySerializer
