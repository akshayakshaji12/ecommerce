from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from medicalapp.models import Company
import medicalapp.serializers
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
