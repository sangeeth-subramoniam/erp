from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from registration.models import user_profile


class Department(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        verbose_name = ('department')
        verbose_name_plural = ('departments')
        # db_table = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name



class Employee(models.Model):
    user_profile = models.ForeignKey(user_profile, on_delete=models.CASCADE, null=True, blank=True )
    emp_no = models.IntegerField( primary_key=True )
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14 , help_text="Enter your First Name")
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()
    address = models.TextField(max_length=100, blank = True, null=True, default="NAN")

    class Meta:
        verbose_name = ('employee')
        verbose_name_plural = ('employees')
        # db_table = 'employees'
    
    def get_absolute_url(self):
        return reverse('homepage:emplist')


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class DeptEmp(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=('department'))
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    

    class Meta:
        verbose_name = ('department employee')
        verbose_name_plural = ('department employees')
        db_table = 'dept_emp'

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class Title(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=('employee'))
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    

    class Meta:
        verbose_name = ('title')
        verbose_name_plural = ('titles')
        # db_table = 'titles'

    def __str__(self):
        return "{} - {}".format(self.employee, self.title)


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=('employee'))
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField(null=True,blank=True)

    

    class Meta:
        # db_table = 'salaries'
        ordering = ['-from_date']
        verbose_name = ('salary')
        verbose_name_plural = ('salaries')

    def __str__(self):
        return "{} - {}".format(self.employee, self.salary)


class DeptManager(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=('department'))
    from_date = models.DateField()
    to_date = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name = ('department manager')
        verbose_name_plural = ('department managers')
        # db_table = 'dept_manager'
        ordering = ['-from_date']

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class attendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=('department'))
    date = models.DateField()

class logs(models.Model):
    logid = models.AutoField(primary_key=True)
    logger = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=50 , blank=True , null = True)
    start_time = models.DateTimeField(blank=True , auto_created=True)
    end_time = models.DateTimeField(blank=True, null=True ,auto_created=True)
    location = models.CharField(max_length=30, blank=True , null=True)

    def __str__(self):
        return str(str(self.logid) + str(self.logger))











