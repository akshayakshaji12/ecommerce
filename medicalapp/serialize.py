from rest_framework import serializers
from medicalapp.models import Company


class HyperlinkedModelSerializer:
    pass


class CompanySerliazer(serializers,HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields=["name","license_no","address","contact_no","email","description"]
