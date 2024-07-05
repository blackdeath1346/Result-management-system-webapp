from django.shortcuts import render
from rest_framework import viewsets
from res_man.serializers import StudentSerializer,CourseSerializer,EnrollmentSerializer
from res_man.models import Student,Course, Enrollment

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = []  # Disable authentication
    permission_classes = []      # Disable permission checks



# Create your views here.
