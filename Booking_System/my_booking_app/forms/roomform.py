from django import forms
from my_booking_app.models.roommodel import Room

# Room
class Room_Details(forms.ModelForm):
    Room_Image = forms.ImageField()

    class Meta:
        model = Room
        fields = "__all__"
