from django.shortcuts import render,redirect

# imports for calendar.
import calendar
from calendar import monthrange
import datetime

from .models import Attendance
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
def create_attendance():
    days_list = []
    for day in range(1,num_days+1):
        days_list.append(day)
                # days_list[day] = "" 
            # print(days_list)
    return days_list
def attendance(request):

    if request.method == "POST":
        print(request.POST)
        emp = Employee.objects.get(user__user__id = request.user.id)
        p_month = str(request.POST.get("month"))
        p_date = str(request.POST.get("date"))
        p_year = str(year)
        print('dflkasf year and month da' , p_month , p_date)
        attendance_instance = Attendance.objects.create(employee = emp , year = p_year , month = p_month , date = p_date)

        return redirect('homepage:home')

    else:
        

        #model cobject a list for the days each time take the list update it and if number not in list put red color 


        days_list = create_attendance()

        
        context = {
            'days_list' : days_list,
            'month' : month_name,
        }
        return render(request,'attendance/attendance_page.html', context)

