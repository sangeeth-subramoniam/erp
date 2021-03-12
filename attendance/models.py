from django.db import models
from structure.models import Employee

# Create your models here.

class Attendance(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE , related_name= "emp_attendance")
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=10)
    date = models.CharField(max_length=2)

