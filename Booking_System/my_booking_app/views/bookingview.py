from django.shortcuts import render, redirect
from django.template import RequestContext
#importing booking form
from my_booking_app.forms.bookingform import Booking_Form
#importing booking model
from my_booking_app.models.bookingmodel import Booking
# for booking record in admin dashboard
def booking_table(request):
    if "next" in request.POST:
        context = {'booking_list': Booking.objects.raw("select * from booking limit 10 offset 10")}
    else:
        context = {'booking_list': Booking.objects.raw("select * from booking limit 10 offset 0")}
    return render(request, 'booking_table.html', context)

#for making a new booking
def bookinginsert(request):
    if request.method == "POST":
        formb = Booking_Form(request.POST)
        formb.save()
        return redirect('room')
    else:
        formb = Booking_Form()
    return render(request, "room.html", {'formb': formb}, context_instance=RequestContext(request))

#for deleting the booking made by customer
def booking_delete(request, id):
    booking = Booking.objects.get(Booking_ID=id)
    booking.delete()
    return redirect('booking_table')

