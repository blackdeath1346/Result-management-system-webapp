from rest_framework import serializers
from res_man.models import Student,Course,Enrollment
#from res_man.models import Course

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields = "__all__"

class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model=Enrollment
        fields = "__all__"
