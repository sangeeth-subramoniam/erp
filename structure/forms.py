from django import forms
from .models import Employee,DeptEmp


class EmployeeUpdateForm(forms.ModelForm):
    #user_profile = forms.CharField(disabled=True)
    emp_no = forms.IntegerField(disabled=True)
    first_name = forms.CharField(max_length=14, disabled=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user_profile',]



class DeptEmpUpdateForm(forms.ModelForm):
    # dept_no = forms.IntegerField(disabled=True)
    employee = forms.CharField(disabled=True)
    
    
    
    class Meta:
        model = DeptEmp
        fields = '__all__'

