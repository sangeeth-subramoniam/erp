from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Employee,DeptEmp
from .forms import EmployeeUpdateForm, DeptEmpUpdateForm


# Create your views here.

class EmployeeUpdate(UpdateView):
    
    
    model = Employee
    form_class = EmployeeUpdateForm
    

class DeptEmpUpdate(UpdateView):
    model = DeptEmp
    form_class = DeptEmpUpdateForm
    
