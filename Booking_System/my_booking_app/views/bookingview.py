from django.shortcuts import render, redirect
from my_booking_app.authenticate import Authenticate
from my_booking_app.forms.bookingform import Booking_Form
from my_booking_app.models.customer import Customer
from my_booking_app.models.room import Room
from my_booking_app.models.booking import Booking
from django.http import HttpResponse, JsonResponse
# booking record
def booking_table(request):
    if "next" in request.POST:
        context = {'booking_list': Booking.objects.raw("select * from booking limit 10 offset 10")}
    else:
        context = {'booking_list': Booking.objects.raw("select * from booking limit 10 offset 0")}
    return render(request, 'booking_table.html', context)


def bookinginsert(request):
    if request.method == "POST":
        formb = Booking_Form(request.POST)
        formb.save()
        return redirect('room')
    else:
        formb = Booking_Form()
    return render(request, "room.html", {'formb': formb})