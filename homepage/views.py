from django.shortcuts import render
from registration.models import user_profile
from structure.models import *

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import userprofile_updateForm


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

# def emplist(request):
#     employee = Employee.objects.all()
#     context = {'emplist':employee}
#     # for items in employee:
#     # print('wewrwer',employee.last_name)
#     return render(request, 'landing/emplist.html',context)

def profile(request):
    curr_user = request.user
    
    employee = Employee.objects.get(user_profile__email = curr_user.email)
    # dept = DeptEmp.objects.all().filter(employee__emp_no = pk)
    dept = DeptEmp.objects.get(employee__user_profile__email = curr_user.email)
    profilepicture = user_profile.objects.get(email=curr_user.email)
    print('i am the profile pic ', profilepicture.profile_picture)
    

    try:
        
        title = Title.objects.get(employee__user_profile__email = curr_user.email)
    
    except:
        title = "Employee"


# manager_status = DeptManager.objects.get(employee__emp_no = pk)
# print(manager_status)
    manager_status = get_or_none(DeptManager,employee__user_profile__email = curr_user.email)
    print(manager_status)
    
        
    # print('detail page ', employee)
    # print('sdkfjahskfj',dept)
    # print('alaya manasa',dept2.department.dept_no)
    # for items in dept:
    #     print('sdkfjahskfj',dept.department)
    return render(request,'landing/profile.html', {'emp' : employee, 'dept' : dept, 'title' : title , 'manager_status' : manager_status , 'pp':profilepicture})
    # except:
    #     error = "UnAppropritae User"
    #     return render(request,'error/errorpage.html', {'error' : error})

    
class updateprofile(UpdateView):
    model = user_profile
    form_class = userprofile_updateForm