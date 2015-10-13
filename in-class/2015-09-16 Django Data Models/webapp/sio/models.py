from django.db import models

# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=200)
    studentid = models.IntegerField(default=0)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.studentname


class Course(models.Model):
    coursename = models.CharField(max_length=200)
    courseid = models.IntegerField(default=0)
    students = models.ManyToManyField(Student)
