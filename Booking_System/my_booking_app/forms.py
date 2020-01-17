from django import forms
from my_booking_app.models import Customer,Room,Booking
class Customer_Signup_Form (forms.ModelForm):
   Password=forms.CharField(widget=forms.PasswordInput)
   class Meta:
      model= Customer
      fields="__all__"
class Room_Details(forms.ModelForm):
   Room_Image=forms.ImageField()
   class Meta:
      model=Room
      fields="__all__"
class Booking_Form(forms.ModelForm):
   class Meta:
      model=Booking
      fields="__all__"