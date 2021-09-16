from django.shortcuts import render
from .forms import User_form , user_profile_form

from datetime import datetime

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import user_profile
from structure.models import logs

from datetime import datetime


from django.contrib.auth.decorators import login_required



#geting client ip address

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    print('xforw is ', x_forwarded_for)
    if x_forwarded_for:
        #ip = x_forwarded_for.split(',')[-1]
        ip = str(x_forwarded_for)
        print('xforward')
    else:
        ip = request.META.get('REMOTE_ADDR')
        print('remote addr')
    return ip



# Create your views here.
def signup(request):
    registered = False

    if request.method == "POST":
        
        user_form = User_form(data=request.POST)
        user_profileform = user_profile_form(data=request.POST)

        if(user_form.is_valid() and user_profileform.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profileform.save(commit=False)
            profile.user = user
            profile.email = user.email

                    
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            
            profile.save()

            registered = True
        
        else:
            print(user_form.errors, user_profileform.errors)
    
    else:
        user_form = User_form()
        user_profileform = user_profile_form()
        

    return render(request, "registration/signup.html", {'user_form': user_form , 'user_profileform' : user_profileform, 'registered' : registered  } )


#sign in
def signin(request):
    context = {}
    
    if(request.method == "POST"):
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user:
            if user.is_active:
                getip = get_client_ip(request)
                print('the ip used is ', getip)
                user_log = logs(logger = username , start_time = datetime.now() , ip = getip, location = 'Japan' )
                user_log.save()
                login(request,user)
                return HttpResponseRedirect(reverse('homepage:home'))

            else:
                return render(request,'registration/signin.html' , context)
            
        else:
            print("someone tried to login and failed")
            print("username: {} and password {}".format(username,password))
            return render(request,"registration/signin_fail_page.html")
    
    else:
        
        return render(request,'registration/signin.html' , context)


@login_required
def signout(request):
    # val = user_profile.objects.get(user_id = request.user.id)
    # print('sdlkjdslf',val.bio)
    logout(request)
    return HttpResponseRedirect(reverse("homepage:home"))