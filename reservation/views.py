from django.shortcuts import render,redirect

from .models import Rooms,Booking

from structure.models import Employee

from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib import messages 


from django.contrib.auth.decorators import login_required

#to check for clashing reservations

import datetime

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


def check_time(current_start_time, current_end_time , t1, t2):
    if t1 < t2:
        if(current_start_time >= t1 and current_start_time <= t2 ):
            return 'False'
                
        elif(current_end_time >=t1 and current_end_time <= t2 ):
            return 'False'
        else:
            return 'True'
    else:
        return 'Error'

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

    print(rooms.room_image)

    return render(request, 'reservation/detail_page.html' , context)

@login_required
def room_reserve(request , pk):

    room = Rooms.objects.get(room_no = pk)

    booking = Booking.objects.all().filter(room__room_no = pk)

    print('room is ',room)

    print('booking are ' , booking)

    ls = []
    for items in booking:
        
        start = str(items.start_time.time())
        end = str(items.end_time.time())
        

        timings = start + ' to ' + end + ' by ' + str(items.employee).upper()

        ls.append(timings)
        print('list is ', ls)
        


    context = {

        'room' : room , 
        'booking' : booking,
        'booked' : ls
    
    }

    return render(request, 'reservation/reservation.html' , context)


class BookingCreate(CreateView):

    # employee = Employee.objects.get(user_profile__email = request.user.email)

    model = Booking
    fields = ['start_time' , 'end_time' , 'status' ]

    def form_valid(self, form):
        form.instance.user = self.request.user

        room_reserve = Rooms.objects.get(room_no=self.kwargs['class'])
        form.instance.room = room_reserve


        form.instance.employee = Employee.objects.get(user_profile__email = self.request.user.email)

        booking = Booking.objects.all().filter(room = form.instance.room)
        accept = 1
        for items in booking:
            t1 = items.start_time.time()
            t2 = items.end_time.time()
            
            current_start_time = form.instance.start_time.time()
            current_end_time = form.instance.end_time.time()
            print('start and end are ', current_start_time,current_end_time)

            acceptance = check_time(current_start_time,current_end_time,t1,t2)
            print('acceptance at ', t1 ,' and ' , t2 , 'is ' , acceptance)
            if(acceptance == 'False'):
                accept = 0
        
        if accept == 0:
            messages.error(self.request, "RESERVATION FAILED ! Please Change the Time. Already booked for the specified time ")
            
        else:
            super(BookingCreate, self).form_valid(form)
            
        return redirect('reservation:home')
            






