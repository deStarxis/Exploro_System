from django import forms
from my_booking_app.models.booking import Booking

# Booking made by Customer
class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


