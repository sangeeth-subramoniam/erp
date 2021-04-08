from django.db import models
from structure.models import Employee

# Create your models here.

class Attendance_details(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE , related_name= "emp_attendance")
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=10)
    date = models.CharField(max_length=2)
    report = models.TextField( max_length= 200 ,blank=True)

    def __str__(self):
        return str(self.employee.user_profile.user)
    

