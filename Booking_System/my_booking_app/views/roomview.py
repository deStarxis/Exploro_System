from django.shortcuts import render, redirect
from my_booking_app.authenticate import Authenticate
from my_booking_app.forms.roomform import Room_Details
from my_booking_app.models.customer import Customer
from my_booking_app.models.room import Room
from my_booking_app.models.booking import Booking
from django.http import HttpResponse, JsonResponse

def room(request):
    context = {'room_list': Room.objects.all()}
    return render(request, 'room.html', context)

def room_table(request):
    if "next" in request.POST:
        context = {'room_list': Room.objects.raw("select * from room limit 2 offset 2")}
    else:
        context = {'room_list': Room.objects.raw("select * from room limit 2 offset 0")}
    return render(request, 'Room_table.html', context)


def room(request):
    context = {'room_list': Room.objects.all()}
    return render(request, 'room.html', context)

def roominsert(request):
    if request.method == "POST":
        formr = Room_Details(request.POST, request.FILES)
        formr.save()
        return redirect('room_table')
    else:
        formr = Room_Details()
    return render(request, "room_insert.html", {'formr': formr})


def room_edit(request, id):
    room = Room.objects.get(Room_ID=id)
    return render(request, 'room_edit.html', {'room': room})


def room_update(request, id):
    room = Room.objects.get(Room_ID=id)
    formr = Room_Details(request.POST, request.FILES, instance=room)
    formr.save()
    return redirect('room_table')


def room_delete(request, id):
    Room.objects.get(Room_ID=id).Room_Image.delete()
    room = Room.objects.get(Room_ID=id)
    room.delete()
    return redirect('room_table')