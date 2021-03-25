from django.shortcuts import render,redirect

from .models import Rooms,Booking

from structure.models import Employee

from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib import messages 


from django.contrib.auth.decorators import login_required

#to check for clashing reservations

import datetime

import datetime
import pytz

utc=pytz.UTC

# DAY, NIGHT = 1, 2
# def check_time(time_to_check, on_time, off_time):
#     if on_time > off_time:
#         if time_to_check > on_time or time_to_check < off_time:
#             return NIGHT, True
#     elif on_time < off_time:
#         if time_to_check > on_time and time_to_check < off_time:
#             return DAY, True
#     elif time_to_check == on_time:
#         return None, True
#     return None, False


# def check_time(current_start_time, current_end_time , t1, t2 , t1_day , current_start_time_day):
#     if(t1_day == current_start_time_day):
#         if t1 < t2:
#             if(current_start_time >= t1 and current_start_time <= t2 ):
#                 return 'False'
                    
#             elif(current_end_time >=t1 and current_end_time <= t2 ):
#                 return 'False'
#             else:
#                 return 'True'
#     elif(t1_day != current_start_time_day)
#         return 'True'
    
#     else:
#         return 'Error'


# def check_time(current_start_time, current_end_time , t1, t2 , t1_day , current_start_time_day):
    
#     print('this is to test values ' , current_start_time,current_end_time,t1,t2,current_start_time_day,t1_day)

    
#     if(t1_day != current_start_time_day):
#         return 'True'    
    
#     else:
#         print('this is to test values ' , current_start_time,current_end_time,t1,t2,current_start_time_day,t1_day)
#         if ((t1 < t2) and (current_start_time < current_end_time)) :
#             if(current_start_time >= t1 and current_start_time <= t2 ):
#                 print('1')
#                 return 'False'
                    
#             elif(current_end_time >=t1 and current_end_time <= t2 ):
#                 print('2')
#                 return 'False'
#             else:
#                 print('3')
#                 return 'True'
#         else:
#             print('4')
#             return 'Error'


def check_time(start_time , end_time, day_val , old_start_time , old_end_time , old_day):

    print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz comparison values : ', start_time, end_time, day_val , ' and ' , old_start_time , old_end_time , old_day )
    print('compare 1 ' , day_val , ' and ' , old_day)
    print('compare 2 ' , start_time , ' and ' , start_time)
    print('compare 2 ' , old_start_time.hour , ' and ' , old_start_time.minute)

    updated_old_start_time = old_start_time.replace(tzinfo=utc)
    updated_old_end_time = old_end_time.replace(tzinfo=utc) 

    updated_start_time = start_time.replace(tzinfo=utc)
    updated_end_time = end_time.replace(tzinfo=utc) 

    print('after updating to local ' , updated_old_start_time , ' and ' , updated_old_end_time)

    if(day_val != old_day):
        print('day ve vera')
        return 1

    elif(updated_end_time <= updated_start_time):
        print('End time is higher than the start time. Error')
        return 3

    else:
        if(  (updated_old_start_time <= updated_start_time <= updated_old_end_time) or (updated_old_start_time <= updated_end_time <= updated_old_end_time)  ):
            print("kurukula vandha kurukelumbula midhichiduven ")
            return 0
        
        else:
            print('kuruka varala over over' )
            return 1




#check for clashing reservation time over





@login_required
# Create your views here.
def home(request):

    rooms = Rooms.objects.all().filter(status = True)

    context = {
        'rooms' : rooms
    }

    return render(request , 'reservation/home.html' , context)

@login_required
def room_details(request , pk):

    rooms = Rooms.objects.get(room_no = pk)

    facilities = str(rooms.facilities).split(',')

    # print(facilities.split(','))

    context = {
        'rooms' : rooms ,
        'facilities' : facilities
    }

    return render(request, 'reservation/detail_page.html' , context)

@login_required
def room_reserve(request , pk):

    now = datetime.datetime.now()

    room = Rooms.objects.get(room_no = pk)

    booking = Booking.objects.all().filter(room__room_no = pk).order_by('start_time')

    ls = []
    for items in booking:
        
        start = str(items.start_time.time())
        end = str(items.end_time.time())

        if items.day == now.day :
            # print('llllllllllllllllllllllllllllllllllllllllllllllllllll now.day is same')
            date = str(datetime.datetime.today())[0:10]# .strftime('%y-%m-%d')
            temp_time = "TODAY"
        else:
            date = str(datetime.datetime.today() + datetime.timedelta(days=1))[0:10]
            temp_time = "TOMORROW"
        

        timings = start + ' to ' + end + ' by ' + str(items.employee).upper() + ' ' + temp_time + ' (' + date + ')'

        ls.append(timings)
        
        


    context = {

        'room' : room , 
        'booking' : booking,
        'booked' : ls
    
    }

    return render(request, 'reservation/reservation.html' , context)


# class BookingCreate(CreateView):

#     # employee = Employee.objects.get(user_profile__email = request.user.email)

#     model = Booking
#     fields = ['start_time' , 'end_time' , 'status' ]

#     def form_valid(self, form):
#         form.instance.user = self.request.user

#         room_reserve = Rooms.objects.get(room_no=self.kwargs['class'])
#         form.instance.room = room_reserve


#         form.instance.employee = Employee.objects.get(user_profile__email = self.request.user.email)

#         booking = Booking.objects.all().filter(room = form.instance.room)
#         accept = 1
#         for items in booking:
#             t1 = items.start_time.time()
#             t2 = items.end_time.time()
            
#             current_start_time = form.instance.start_time.time()
#             current_end_time = form.instance.end_time.time()
#             print('start and end are ', current_start_time,current_end_time)

#             acceptance = check_time(current_start_time,current_end_time,t1,t2)
#             print('acceptance at ', t1 ,' and ' , t2 , 'is ' , acceptance)
#             if(acceptance == 'False'):
#                 accept = 0
        
#         if accept == 0:
#             messages.error(self.request, "RESERVATION FAILED ! Please Change the Time. Already booked for the specified time ")
            
#         else:
#             super(BookingCreate, self).form_valid(form)
            
#         return redirect('reservation:home')


def BookingCreate(request , pk):

    if request.method == "POST":

        now = datetime.datetime.now()

        user = request.user
        employee = Employee.objects.get(user_profile__email = user.email)
        room = Rooms.objects.get(room_no = pk)

        today_or_tomorrow = request.POST.get("day")
        if today_or_tomorrow == "today":
            day_val = int(now.day)
        else:
            day_val = int(now.day + 1)
        
        
        start_hours = int(request.POST.get('start_hours'))
        start_minutes = int(request.POST.get('start_minutes'))

        start_time = datetime.datetime(now.year,now.month,day_val,start_hours,start_minutes,00)

        end_hours = int(request.POST.get('end_hours'))
        end_minutes = int(request.POST.get('end_minutes'))

        end_time = datetime.datetime(now.year, now.month , day_val , end_hours , end_minutes , 00)


        bookings = Booking.objects.all().filter(room = room)

        if not bookings:
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa empty we can create')
            Booking.objects.create(user = user, employee = employee ,day = day_val , room = room , start_time=  start_time , end_time = end_time , status = True)
            

        else:
            print('bbbbbbbbbbbbbbbbbbbb not empty we have to check')
            verdictls = []
            for instances in bookings:
                verdictls.append(check_time(start_time,end_time,day_val,instances.start_time,instances.end_time,instances.day))
            if(0 in verdictls):
                print('fffffffffffffffffffffffffffffffffffailed ' , verdictls)
                error = 'Your Timing clashes with already booked schedule. Please change the time. Check the previous page for already booked timings'
                return render(request, "reservation/bookingcreate.html" , { 'error' : error , 'room' : room })

            if(3 in verdictls):
                print('fffffffffffffffffffffffffffffffffffailed ' , verdictls)
                error = 'End time is earlier thatn the Start time. Please change the times to continue'
                return render(request, "reservation/bookingcreate.html" , { 'error' : error , 'room' : room })


            else:
                Booking.objects.create(user = user, employee = employee ,day = day_val , room = room , start_time=  start_time , end_time = end_time , status = True)
                print('created aftercheckkkkkkkkkkkkkkkkkkkkkkkkkkkkk')





            

        return redirect('reservation:home')

    else:
        employee = Employee.objects.get(user_profile__email = request.user.email)

        room = Rooms.objects.get(room_no = pk)

        return render(request,'reservation/bookingcreate.html' , { 'room' : room})




def schedule(request, pk):

    bookings = Booking.objects.all().filter(user__email = pk)

    context = {
        'bookings' : bookings
    }

    return render(request,'reservation/schedule.html', context)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if request.method == "POST":

    #     now = datetime.datetime.now()

    #     start_hours = request.POST.get('start_hours')

    #     day_name = request.POST.get('day')

    #     start_minutes = request.POST.get('start_minutes')

    #     end_hours = request.POST.get('end_hours')

    #     end_minutes = request.POST.get('end_minutes')


    #     if(day_name == "today"):
    #         day_value = int(now.day)
        
    #     else:
    #         day_value = int(now.day + 1 )


    #     year = int(now.year)

    #     month = int(now.month)

    #     form_start_time = datetime.datetime(year,month,day_value,int(start_hours),int(start_minutes),00)

    #     form_end_time = datetime.datetime(year,month,day_value,int(end_hours),int(end_minutes),00)
        

    #     user = request.user
    #     room = Rooms.objects.get(room_no = pk)
    #     employee = Employee.objects.get(user_profile__email = user.email)
    #     status = True



    #     booking = Booking.objects.all().filter(room = room)
    #     accept = 1

    #     for items in booking:
    #         t1 = items.start_time.time()
    #         t2 = items.end_time.time()
    #         t1_day = items.day
            
            
    #         current_start_time = form_start_time.time()
    #         current_end_time = form_end_time.time()
    #         current_start_time_day = form_start_time.day

    #         acceptance = check_time(current_start_time,current_end_time,t1,t2 , t1_day , current_start_time_day)
            
    #         if(acceptance == 'False'):
    #             accept = 0
    #         if(acceptance == 'error'):
    #             accept = 3

        
    #     if(form_start_time == form_end_time):
    #         error =  "Same Start and End time. Please Change ! "
    #         return render(request, "reservation/bookingcreate.html" , { 'error' : error })
        
    #     elif accept == 0:
    #         error = "RESERVATION FAILED ! Please Change the Time. Already booked for the specified time "
    #         return render(request, "reservation/bookingcreate.html" , { 'error' : error , 'room' : room })
        
    #     elif accept == 3:
    #         error = "Please Check the Time format"
    #         return render(request, "reservation/bookingcreate.html" , { 'error' : error , 'room' : room })
            
    #     else:
    #         # print(user,employee,room,current_start_time,current_end_time,status)
    #         booking_instance = Booking.objects.create(user = user, employee = employee ,day = day , room = room , start_time=  form_start_time , end_time = form_end_time , status = status )
    #         return redirect('reservation:home')

    # else:
            
    #     employee = Employee.objects.get(user_profile__email = request.user.email)

    #     room = Rooms.objects.get(room_no = pk)





    #     return render(request,'reservation/bookingcreate.html' , { 'room' : room})







