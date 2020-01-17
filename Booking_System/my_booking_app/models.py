from django.db import models
class Customer(models.Model):
    ID=models.AutoField(auto_created=True,primary_key=True)
    Fullname=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    Mobile = models.CharField(max_length=15)
    Password=models.CharField(max_length=50)
    class Meta:
        db_table="customer"
class Room(models.Model):
    Room_ID=models.AutoField(auto_created=True,primary_key=True)
    Room_Image=models.ImageField(default="")
    ROOM_TYPES = (
        ("Single Room","Single Room"),
        ("Double Room","Double Room"),
        ("Double Double Room","Double Double Room"),
        ("Twin Room","Twin Room"),
        ("Interconnecting Rooms","Interconnecting Rooms"),
        ("Adjoining Rooms","Adjoining Rooms"),
        ("Duplex","Duplex"),
        ("Cabana","Cabana"),
        ("Studio Room","Studio Room"),
        ("Parlor","Parlor"),
        ("Lanai","Lanai"),
        ("Efficiency Room","Efficiency Room"),
        ("Hospitality Room","Hospitality Room"),
        ("Suite Room","Suite Room"),
        ("King Bedroom","King Bedroom"),
        ("Queen Bedroom","Queen Bedroom")
    )
    Room_Type=models.CharField(choices=ROOM_TYPES,default="",max_length=50)
    Location=models.CharField(max_length=200)
    Price=models.CharField(max_length=10)
    Description=models.TextField(max_length=500,null=False,default="")
    class Meta:
        db_table="room"
class Booking(models.Model):
    Booking_ID=models.AutoField(auto_created=True,primary_key=True)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Room=models.ForeignKey(Room,on_delete=models.CASCADE)
    Date_of_Booking=models.DateField
    No_of_Rooms_Booked=models.CharField(max_length=2)
    Total_Price=models.CharField(max_length=10)
    class Meta:
        db_table="booking"