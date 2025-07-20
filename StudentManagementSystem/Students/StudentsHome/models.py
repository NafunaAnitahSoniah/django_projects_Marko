from django.db import models

# Create your models here.

class Student(models.Model):
    names = models.CharField(max_length=255)
    gender = models.CharField(max_length=10) #Male or Female
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone = models.CharField(max_length=15)
    course = models.TextField()
    result = models.IntegerField()
    student_id = models.CharField(max_length=15)



