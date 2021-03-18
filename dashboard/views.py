from django.shortcuts import render,redirect
from .models import Message

from django.contrib import messages

from structure.models import Employee

from registration.models import user_profile
# Create your views here.
def home(request):

    if request.method == "POST":
        curr_user = request.user

        current_user = curr_user
        up = user_profile.objects.get(user = curr_user)
        print('up is ,' , up)
        emp = Employee.objects.get(user_profile__email = curr_user.email)
        print('emp is ', emp)
        message_content = request.POST['message']
        print('message content is ', message_content)
        sender = curr_user
        reciever = Employee.objects.get(emp_no = 0)
        print(reciever)
        important = request.POST.get('important')
        if(important == "on"):
            important = True
        else:
            important = False
        

        # reciever = Employee.objects.get(user_profile__email = current_user.email)
        

        Message.objects.create(user = curr_user, user_profile = up , employee = emp , message = message_content , sender = emp , reciever = reciever, important=important) 
        print('Message object created !')
        
        return redirect('dashboard:home')




    curr_user = request.user
    admin = Employee.objects.get(emp_no = 0)
    print('admin is ', admin)
    messages = Message.objects.all().filter(reciever=admin).order_by('-created_at')
    print(messages)
    return render(request,'dashboard/dashboard.html', {'messages': messages, 'curr_user' : curr_user})


def delete(request,pk):

    message = Message.objects.get(id = pk)
    print(message)
    if(message.employee.user_profile.user == request.user) : 

        message.delete()
        print('message deleted')
    
    else:
        messages.error(request,'You cannot delete others post')

    return redirect('dashboard:home')


    # message for deleting others @post pending

    