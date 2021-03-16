from django.shortcuts import render
from .models import Message
# Create your views here.
def home(request):
    messages = Message.objects.all()
    return render(request,'dashboard/dashboard.html', {'messages': messages})