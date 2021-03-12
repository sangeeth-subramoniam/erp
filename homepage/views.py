from django.shortcuts import render
from registration.models import user_profile
from structure.models import *


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        curruser = request.user
        return render(request,'landing/homepage.html',{'curr_user' : curruser})
    else:
        return render(request,'landing/homepage.html')

def contact(request):
    return render(request,'landing/contact.html')

def about(request):
    return render(request,'landing/about.html')

def emplist(request):
    employee = Employee.objects.all()
    context = {'emplist':employee}
    # for items in employee:
    # print('wewrwer',employee.last_name)
    return render(request, 'landing/emplist.html',context)

def emp_detail(request,pk):
    employee = Employee.objects.all().filter(emp_no = pk)
    # dept = DeptEmp.objects.all().filter(employee__emp_no = pk)
    dept = DeptEmp.objects.get(employee__emp_no = pk)

    title = Title.objects.get(employee__emp_no = pk)

    # manager_status = DeptManager.objects.get(employee__emp_no = pk)
    # print(manager_status)
    manager_status = get_or_none(DeptManager,employee__emp_no = pk)
    print(manager_status)
    
        
    # print('detail page ', employee)
    # print('sdkfjahskfj',dept)
    # print('alaya manasa',dept2.department.dept_no)
    # for items in dept:
    #     print('sdkfjahskfj',dept.department)
    return render(request,'landing/emp_detail.html', {'emp_detail' : employee, 'dept' : dept, 'title' : title , 'manager_status' : manager_status})
