from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

# Create Get(list) and Post(creat)
class PatientList(generics.ListCreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Create Put(edit) and Delete()
class PatientEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer