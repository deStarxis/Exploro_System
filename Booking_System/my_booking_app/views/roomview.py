from django.shortcuts import render, redirect
#importing room form
from my_booking_app.forms.roomform import Room_Details
#importing room model
from my_booking_app.models.roommodel import Room

#for room page
def room(request):
    context = {'room_list': Room.objects.all()}
    return render(request, 'room.html', context)

#for viewing the room details in admin dashboard
def room_table(request):
    if "next" in request.POST:
        context = {'room_list': Room.objects.raw("select * from room limit 8 offset 8")}
    else:
        context = {'room_list': Room.objects.raw("select * from room limit 8 offset 0")}
    return render(request, 'Room_table.html', context)

#for adding a new room
def roominsert(request):
    if request.method == "POST":
        formr = Room_Details(request.POST, request.FILES)
        formr.save()
        return redirect('room_table')
    else:
        formr = Room_Details()
    return render(request, "room_insert.html", {'formr': formr})

#for editing an existing room
def room_edit(request, id):
    room = Room.objects.get(Room_ID=id)
    return render(request, 'room_edit.html', {'room': room})

#for updating the details of a room
def room_update(request, id):
    room = Room.objects.get(Room_ID=id)
    formr = Room_Details(request.POST, request.FILES, instance=room)
    formr.save()
    return redirect('room_table')

#for deleting a room
def room_delete(request, id):
    Room.objects.get(Room_ID=id).Room_Image.delete()
    room = Room.objects.get(Room_ID=id)
    room.delete()
    return redirect('room_table')