from django.shortcuts import render,reverse,redirect
from .models import Messaging
from structure.models import Employee
from registration.models import user_profile
#for chaining lists
from itertools import chain
from operator import attrgetter

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    if request.method == 'POST':

        name = request.POST.get('employee_search')
        
        if(name == "all"):
            employees = Employee.objects.all().exclude(user_profile__email = request.user.email)
    

        else:
            employees = Employee.objects.filter(first_name__icontains=name).exclude(user_profile__email = request.user.email)

        context = {
            'employees' : employees
        }

        return render(request,"messaging/searchpage.html", context)
        


    # messages = Messaging.objects.all().order_by('-created_at')
    # my_messages = Messaging.objects.all().filter(reciever__user_profile__user__id = request.user.id).values('sender').distinct()
    my_messages = Messaging.objects.all().filter(reciever__user_profile__user__id = request.user.id).order_by('-created_at')
    # for messages in my_messages:
    #     print(messages.sender)

    senderls = []
    sender_id_ls = []

    for items in my_messages:

        if items.sender not in senderls:
            senderls.append(items.sender)
            

    print('type ' , senderls)


    context = {
        'my_messages' : my_messages,
        'sender_list' : senderls
    }

    return render(request , 'messaging/message.html' , context)


def chat(request,pk):
    
    if request.method == "POST":
        
        current_user = request.user
        up = user_profile.objects.get(user = current_user)
        print('up is ,' , up)
        emp = Employee.objects.get(user_profile__email = current_user.email)
        print('emp is ', emp)
        message_content = request.POST['message']
        print('message content is ', message_content)
        # sender = current_user
        reciever = Employee.objects.get(emp_no = pk)
        print(reciever)
        important = request.POST.get('important')
        if(important == "on"):
            important = True
        else:
            important = False
        

        # reciever = Employee.objects.get(user_profile__email = current_user.email)
        

        Messaging.objects.create(user = current_user, user_profile = up , employee = emp , message = message_content , sender = emp , reciever = reciever, important=important) 
        print('Message object created !')
        
        return redirect('messaging:chat' , pk=reciever.emp_no)










    sender_msg = Messaging.objects.all().filter(reciever__user_profile__user=request.user , sender__emp_no = pk)

    reciever_msg = Messaging.objects.all().filter(sender__user_profile__user=request.user , reciever__emp_no = pk)

    curr_user = request.user
    curr_user_emp = Employee.objects.get(user_profile__email = curr_user.email)

    result_list = sorted(
    chain(sender_msg, reciever_msg),
    key=attrgetter('created_at') , reverse=True)

    print('sender msg ', curr_user)
    print('reciever msg ', curr_user_emp)

    print(result_list)

    context = {
        'curr_user' : curr_user ,
        'curr_user_employee' : curr_user_emp ,
        'msg_list' : result_list ,
        'pk_no' : pk ,
    }

    return render(request,'messaging/chat.html' , context)


# def search(request,name):


#     employees = Employee.objects.filter(first_name__icontains=name).exclude(user_profile__email = request.user.email)

#     context = {
#         'employees' : employees
#     }

#     return render(request,"messaging/searchpage.html", context)
