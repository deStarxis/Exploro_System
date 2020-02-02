from django.shortcuts import render, redirect
from django.db.models import Q
from my_booking_app.models import Customer
from django.contrib import messages

class Authenticate:
    def valid_user(function):
        def wrap(request, id):
            try:
                Customer.objects.get(Q(Email=request.session['Email']) & Q(Password=request.session['Password']))
                return function(request, id)
            except:
                messages.warning(request, "Wrong Credentials")
                return redirect("/index")

        return wrap
