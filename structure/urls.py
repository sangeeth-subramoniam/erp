from django.urls import path,include
from . import views
from .views import EmployeeUpdate,DeptEmpUpdate

app_name = 'structure'

urlpatterns = [
    path('emp/<int:pk>/', EmployeeUpdate.as_view(), name='EmployeeUpdate'),
    path('empdept/<int:pk>/', DeptEmpUpdate.as_view(), name='DeptEmpUpdate'),
    
]