from django.db import models
from structure.models import Employee

# Create your models here.
class Tickets(models.Model):
    employee = models.ForeignKey(Employee , on_delete = models.CASCADE , related_name="ticket_employee")
    query = models.CharField(max_length=200)
    sender = models.ForeignKey(Employee , on_delete = models.CASCADE , related_name="ticket_sender")
    reciever = models.ForeignKey(Employee , on_delete = models.CASCADE , blank = True, null= True ,  related_name="ticket_reciever")


