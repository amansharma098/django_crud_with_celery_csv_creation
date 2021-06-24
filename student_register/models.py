from __future__ import unicode_literals
from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ApiCount(models.Model):
    api_url = models.CharField(max_length=100,null=True,blank=True)

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    course= models.ForeignKey(Courses,on_delete=models.CASCADE)
