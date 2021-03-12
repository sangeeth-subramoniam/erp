from django.urls import path,include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home , name = "home"),
    path('contact', views.contact , name = "contact"),
    path('about', views.about , name = "about"),

    path('emplist', views.emplist , name = "emplist"),
    path('emp_detail/<int:pk>', views.emp_detail , name = "emp_detail"),
]
