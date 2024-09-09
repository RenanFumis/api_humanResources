
from rest_framework import generics
from validation.models import Employee_card_creation
from validation.serializers import Employee_cardSerializer


class Employee_card_creation(generics.ListCreateAPIView):
    queryset = Employee_card_creation.objects.all()
    serializer_class = Employee_cardSerializer


