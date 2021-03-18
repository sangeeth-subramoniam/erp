from django.db import models
from django.contrib.auth.models import User
from registration.models import user_profile
from structure.models import Employee


# Create your models here.
class Messaging(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "emp_messaging")
    user_profile = models.ForeignKey(user_profile, on_delete=models.CASCADE , related_name= "user_profile_messaging")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE , related_name= "emp_messaging")
    
    message = models.TextField(max_length=300)
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE , related_name= "emp_sender_messaging")
    reciever = models.ForeignKey(Employee, on_delete=models.CASCADE , related_name= "emp_reciever_messaging" , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    important = models.BooleanField(blank = True, null=True)


    def __str__(self):
        name = str(self.sender) +' ' +  str(self.message)[0:10]
        return str(name)