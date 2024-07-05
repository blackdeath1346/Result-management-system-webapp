from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
#from django.db.models.signals import m2m_changed
#from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100,unique=True)
    id = models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)

class Course(models.Model):
    course_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    students=models.ManyToManyField(Student)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.FloatField(default=-1.0)


    class Meta:
        unique_together = ('student', 'course')

@receiver(m2m_changed, sender=Course.students.through)
def create_enrollment(sender, instance, action, reverse, pk_set, **kwargs):
    if action == "post_add":
        for student_id in pk_set:
            student = Student.objects.get(pk=student_id)
            Enrollment.objects.get_or_create(student=student, course=instance)




