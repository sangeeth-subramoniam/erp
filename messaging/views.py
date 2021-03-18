from django.shortcuts import render
from .models import Messaging

# Create your views here.
def home(request):


    # messages = Messaging.objects.all().order_by('-created_at')
    # my_messages = Messaging.objects.all().filter(reciever__user_profile__user__id = request.user.id).values('sender').distinct()
    my_messages = Messaging.objects.all().filter(reciever__user_profile__user__id = request.user.id).order_by('sender')
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

    sender_msg = Messaging.objects.all().filter(reciever__user_profile__user=request.user , sender__emp_no = pk)

    context = {
        'sender_msg' : sender_msg
    }

    return render(request,'messaging/chat.html' , context)