from django.shortcuts import render,redirect
from registration.models import user_profile
from structure.models import *

from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import userprofile_updateForm

from .models import Tickets,Notifications

from django.contrib.auth.decorators import login_required

from django.db.models import Q

from structure.models import DeptEmp, Employee

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

def notifications(request):

    if request.method == "POST" :
        notification_title = request.POST.get('title')
        notification_desc = request.POST.get('message')

        employee = Employee.objects.get(user_profile__email = request.user.email)
        sender = employee


        notification_instance = Notifications.objects.create(employee=employee, notification_title=notification_title , notification_desc=notification_desc , sender=sender)

        return redirect('homepage:notifications')

    else:
        notifications = Notifications.objects.all().order_by('-created_at')
        accessed_by = DeptEmp.objects.get(employee__user_profile__email = request.user.email)
        print(accessed_by)
        if(accessed_by.department.dept_name == 'Admin'):
            admin = 1
        else:
            admin = 0
        print('admin value is ', admin)
        context = {
            'notifications' : notifications ,
            'admin' : admin ,
        }

        return render(request,'landing/notifications.html' , context)

    # def emplist(request):
    #     employee = Employee.objects.all()
    #     context = {'emplist':employee}
    #     # for items in employee:
    #     # print('wewrwer',employee.last_name)
    #     return render(request, 'landing/emplist.html',context)

def profile(request):
    curr_user = request.user
    
    try:
        employee = Employee.objects.get(user_profile__email = curr_user.email)
        # dept = DeptEmp.objects.all().filter(employee__emp_no = pk)
        dept = DeptEmp.objects.get(employee__user_profile__email = curr_user.email)
        profilepicture = user_profile.objects.get(email=curr_user.email)
        print('i am the profile pic ', profilepicture.profile_picture)
    
    except:
        error = "Your Employee credentials are not setup yet. Pleases contact Admin! Sorry for the inconvienience profile test !!"
        return render(request,'error/errorpage.html',{'error' : error})

    

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
    return render(request,'landing/profile.html', {'emp' : employee, 'dept' : dept, 'title' : title , 'manager_status' : manager_status , 'pp':profilepicture , 'curr_user' : curr_user , 'img' : '/dp/test1.jpg' })
    # except:
    #     error = "UnAppropritae User"
    #     return render(request,'error/errorpage.html', {'error' : error})

    
class updateprofile(UpdateView):
    model = user_profile
    form_class = userprofile_updateForm


def tickets(request):

    
    if request.method == "POST":

        admin = Employee.objects.get(emp_no = 0)

        try:

            employee_ticket = Employee.objects.get(user_profile__email = request.user.email)

            ticket = request.POST.get('ticket')

            sendto = request.POST.get('reciever')
            print(sendto)
            sendto = admin
            print('sendto 2' , sendto)

            new_ticket = Tickets.objects.create(employee=employee_ticket, query=ticket , sender = employee_ticket , reciever= sendto)

            return redirect('homepage:tickets')
    
        except:
            error = "Your Employee credentials are not setup yet. Pleases contact Admin! Sorry for the inconvienience !!"
            return render(request,'error/errorpage.html',{'error' : error})
    
    
    
    current_user = request.user
    admin = Employee.objects.get(emp_no = 0)
    ticket = Tickets.objects.all().filter(~Q(status=3)).filter(employee__user_profile__email = current_user.email).order_by('-created_at')
    print(ticket)

    return render(request,'landing/tickets.html', {'tickets' : ticket , 'curr_user' : current_user , 'admin':admin})

def ticket_status(request,pk1,pk2):
    tick = Tickets.objects.get(id = pk1)
    print('value before update' , tick.status)
    tick_upd = Tickets.objects.filter(id=pk1).update(status=pk2)
    print('value after update' , tick.status)

    return redirect('homepage:tickets')


    

def upcoming_modules(request):
    return render(request,'landing/upcoming_modules.html')

