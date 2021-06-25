from student_register.models import *
from django.shortcuts import render
from rest_framework import generics
from . serializers import CreateSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateSerializer

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = CreateSerializer
