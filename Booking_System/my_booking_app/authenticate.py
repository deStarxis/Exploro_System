from django.shortcuts import render, redirect
from django.db.models import Q
#importing customer model
from my_booking_app.models.customermodel import Customer
from django.contrib import messages

#for authenitcation of the user while logging in and logging out

class Authenticate:
    def valid_user(function):
        def wrap(request, id):
            try:
                #storing the email and password of the customer in session
                Customer.objects.get(Q(Email=request.session['Email']) & Q(Password=request.session['Password']))
                return function(request, id)
            except:
                #message displayed after the collapse of session
                messages.warning(request, "Login session expired!! Please Login Again")
                return redirect("/index")
        return wrap




