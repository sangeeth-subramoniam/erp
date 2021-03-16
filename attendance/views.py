from django.shortcuts import render,redirect
from django.contrib import messages 

# imports for calendar.
import calendar
from calendar import monthrange
import datetime

from .models import Attendance_details
from structure.models import Employee

now = datetime.datetime.now()

year = now.year
month_number = now.month
month_name = calendar.month_name[3]

num_days = monthrange(year,month_number)[1]
#print(num_days)
# days_list = []
# for day in range(1,num_days+1):
#     days_list.append(day)

# print(days_list)

def attendance(request):

    if request.method == "POST":

        curr_user = request.user

        val = request.POST['date'][-2:]
        tod = str(now.date())[-2:]
        if val != tod:
            # error = "Contact Admin to mark attendance for anyday other than today"
            messages.error(request, "Contact Admin to mark attendance for anyday other than today")
            return redirect('attendance:attendance')
        else:
            value = Attendance_details.objects.get(employee__user_profile__email = curr_user.email)
            print('empt' , value.report)
            print('check ' , str(val) , str(value.report).split(','))
            if(val in str(value.report).split(',')):
                print('val is ', val , 'list is ', str(value.report).split((',')))
                messages.error(request,'already entered')
                return redirect('attendance:attendance')
            else:
                temp = value.report
                if(str(temp) == ""):
                    temp = temp + str(val)
                else:
                    temp = temp + ','+ str(val)
                
                val_upd = Attendance_details.objects.filter(employee__user_profile__email = curr_user.email).update(report=temp)
            





    curr_user = request.user
    print('idhu ' ,curr_user)
    print('hola hola , ' , curr_user.email)
    print('hela hela ', Employee.user_profile)

    emp = Employee.objects.get(user_profile__email = curr_user.email)
    print(emp)

    return render(request,'attendance/attendance_page.html',{'emp' : emp})




def check_attendance(request):
    curr_user = request.user
    user_attendance = Attendance_details.objects.get(employee__user_profile__email = curr_user.email)
    attended = []
    unattended = []
    val = (user_attendance.report).split(',')
    print(val)
    tod = str(now.date())[-2:]
    for i in range(1,int(tod)+1):
        if(str(i) in val):
            attended.append(i)
        else:
            unattended.append(i)
    return render(request , 'attendance/check_attendance.html' , {'attended' : attended , 'unattended' : unattended})




