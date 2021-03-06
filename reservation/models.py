from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from structure.models import Employee

import datetime

now = datetime.datetime.now()


# Create your models here.
class Rooms(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)

    room_no = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=30)

    facilities = models.CharField(max_length=50 , default="Nan")

    room_image = models.ImageField(upload_to='rooms' , blank = True)

    status = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.room_no) + ' ' + str(self.room_name))

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)

    employee = models.ForeignKey(Employee , on_delete = models.CASCADE)

    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)

    day = models.IntegerField(default=now.day)

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()    

    status = models.BooleanField(default = True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return (str(self.employee) + ' ' + str(self.start_time.time()) + ' to ' +  str(self.end_time.time()) )

    def get_absolute_url(self):
        return reverse('reservation:home')