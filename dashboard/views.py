from django.shortcuts import render,redirect
from .models import Message

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

        # reciever = Employee.objects.get(user_profile__email = current_user.email)
        

        Message.objects.create(user = curr_user, user_profile = up , employee = emp , message = message_content , sender = emp , reciever = None)
        print('Message object created !')
        
        return redirect('dashboard:home')




    curr_user = request.user
    messages = Message.objects.all()
    return render(request,'dashboard/dashboard.html', {'messages': messages, 'curr_user' : curr_user})


def delete(request,pk):

    message = Message.objects.get(id = pk)
    print(message)
    message.delete()
    print('message deleted ')
    return redirect('dashboard:home')