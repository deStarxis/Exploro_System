from django.conf import settings
from django.db import models
from datetime import date

#booking table
class Booking(models.Model):
    Booking_ID = models.AutoField(auto_created=True, primary_key=True)
    Date_of_Booking= models.DateField(default=date.today)
    Customer= models.CharField(default=False,max_length=50)
    Room=models.CharField(default=False,max_length=50)
    No_of_Rooms_Booked = models.CharField(max_length=5)
    
    class Meta:
        db_table = "booking"

