from django.db import models
#room table
class Room(models.Model):
    Room_ID = models.AutoField(auto_created=True, primary_key=True)
    Room_Image = models.ImageField(default="")
    ROOM_TYPES = (
        ("Single Room", "Single Room"),
        ("Double Room", "Double Room"),
        ("Double Double Room", "Double Double Room"),
        ("Twin Room", "Twin Room"),
        ("Interconnecting Rooms", "Interconnecting Rooms"),
        ("Adjoining Rooms", "Adjoining Rooms"),
        ("Duplex", "Duplex"),
        ("Cabana", "Cabana"),
        ("Studio Room", "Studio Room"),
        ("Parlor", "Parlor"),
        ("Lanai", "Lanai"),
        ("Efficiency Room", "Efficiency Room"),
        ("Hospitality Room", "Hospitality Room"),
        ("Suite Room", "Suite Room"),
        ("King Bedroom", "King Bedroom"),
        ("Queen Bedroom", "Queen Bedroom")
    )
    Room_Type = models.CharField(choices=ROOM_TYPES, default="", max_length=50)
    Location = models.TextField(max_length=200, null=False)
    Price = models.CharField(max_length=10)
    Description = models.TextField(max_length=5000, null=False, default="")

    class Meta:
        db_table = "room"