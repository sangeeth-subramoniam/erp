from django.shortcuts import render

from .models import Rooms,Booking

from structure.models import Employee

from django.contrib.auth.models import User

# Create your views here.
def home(request):

    rooms = Rooms.objects.all().filter(status = True)

    context = {
        'rooms' : rooms
    }

    return render(request , 'reservation/home.html' , context)


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


def room_reserve(request , pk):

    room = Rooms.objects.get(room_no = pk)

    booking = Booking.objects.all().filter(room__room_no = pk)

    print('room is ',room)

    print('booking are ' , booking)

    ls = []
    for items in booking:
        
        start = str(items.start_time.time())
        end = str(items.end_time.time())
        

        timings = start + ' to ' + end + ' by ' + str(items.employee).capitalize()

        ls.append(timings)
        print('list is ', ls)
        


    context = {

        'room' : room , 
        'booking' : booking,
        'booked' : ls
    
    }

    return render(request, 'reservation/reservation.html' , context)








