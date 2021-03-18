from django.db import models
from structure.models import Employee
from django.utils.timezone import now

# Create your models here.
class Tickets(models.Model):
    employee = models.ForeignKey(Employee , on_delete = models.CASCADE , related_name="ticket_employee")
    query = models.CharField(max_length=200)
    sender = models.ForeignKey(Employee , on_delete = models.CASCADE , related_name="ticket_sender")
    reciever = models.ForeignKey(Employee , on_delete = models.CASCADE , blank = True, null= True ,  related_name="ticket_reciever")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default = 0)
    # created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.query
    


