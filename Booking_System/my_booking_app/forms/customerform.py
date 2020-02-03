from django import forms
from my_booking_app.models.customer import Customer

# Customer
class Customer_Signup_Form(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = "__all__"


class loginform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"