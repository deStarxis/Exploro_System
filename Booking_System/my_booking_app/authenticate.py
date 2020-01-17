# from django.shortcuts import render,redirect
# from my_booking_app.models import Customer
# from django.contrib import messages
#
# class Authenticate:
#     def valid_user(function):
#         def wrap(request):
#             try:
#                 customer=Customer.objects.get(Email=request.session['Email'])
#                 customer=Customer.objects.get(Password=request.session['Password'])
#                 return function(request)
#             except:
#                 messages.warning(request,"Please Login First")
#                 return redirect("")
#         return wrap