from django.urls import path,include
from . import views
app_name = 'attendance'

urlpatterns = [
    path('', views.attendance , name = "attendance"),
    path('check_attendance', views.check_attendance, name = "check_attendance"),
]