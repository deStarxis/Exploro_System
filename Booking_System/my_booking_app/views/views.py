from django.shortcuts import render, redirect
#importing the models
from my_booking_app.models.bookingmodel import Booking
from my_booking_app.models.customermodel import Customer
from my_booking_app.models.roommodel import Room
#for home page
def index(request):
    return render(request, 'index.html')
#for about us page
def about(request):
    return render(request, 'about.html')
#for privacy page
def privacy(request):
    return render(request, 'privacy.html')
#for admin page
def admin(request):
    return render(request, "admin.html",
                  {'customers': Customer.objects.raw("select * from customer order by ID desc  limit 0,1"),
                   'rooms': Room.objects.raw("select * from room order by Room_ID desc  limit 0,1"),
                   'bookings': Booking.objects.raw("select * from booking order by Booking_ID desc  limit 0,1")})
#for logging out from admin dashboard
def logout(request):
    del request.session['Email']
    del request.session['Password']
    return redirect("index")





