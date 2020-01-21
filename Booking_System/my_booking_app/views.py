from django.shortcuts import render,redirect
from .forms import Customer_Signup_Form,Room_Details,Booking_Form
from .models import Customer,Room,Booking
from django.http import HttpResponse,JsonResponse
# from .authenticate import Authenticate
def index(request):
    return render(request, 'index.html')
def room(request):
    context = {'room_list': Room.objects.all()}
    return render(request, 'room.html',context)
def customerdashboard(request,id):
    customer = Customer.objects.get(ID=id)
    return render(request, 'customer_dashboard.html', {'customer': customer})
def about(request):
    return render(request, 'about.html')
def help(request):
    return render(request, 'help.html')
def privacy(request):
    return render(request, 'privacy.html')
def admin(request):
    return render(request, 'admin.html')
def logincheck(request):
    username=request.POST["Email"]
    password=request.POST["Password"]
    if(username=="admin@gmail.com"):
        if(password=="admin123"):
            return render(request,'admin.html')
    else:
        customers=Customer.objects.get(Email=username,Password=password)
        if(customers.Password==password):
            return render(request,"customer_dashboard.html")
# def customer_entry(request):
#     request.session['Email']=request.POST['Email']
#     request.session['Password']=request.POST['Password']
#     return redirect("index page")
def customersignup(request):
    if request.method == "POST":
        formc=Customer_Signup_Form(request.POST,request.FILES)
        formc.save()
        return redirect("/index")
    else:
        formc=Customer_Signup_Form()
    return render(request,"index.html",{'formc':formc})
# admin page
#customer record
def customer_table(request):
    context = {'customer_list': Customer.objects.all()}
    return render(request, "customer_table.html", context)
def customersearch(request):
	customer=Customer.objects.filter(Email=request.GET['searchbar_customer']).values()
	return JsonResponse(list(customer),safe=False)
#room record
def room_table(request):
    context = {'room_list': Room.objects.all()}
    return render(request, 'Room_table.html',context)
def roominsert(request):
    if request.method == "POST":
        formr=Room_Details(request.POST,request.FILES)
        formr.save()
        return redirect('room_table')
    else:
        formr=Room_Details()
    return render(request,"room_insert.html",{'formr':formr})
def room_edit(request,id):
    room=Room.objects.get(Room_ID=id)
    return render(request,'room_edit.html',{'room':room})
def room_update(request,id):
    room = Room.objects.get(Room_ID=id)
    formr = Room_Details(request.POST,request.FILES, instance=room)
    formr.save()
    return redirect('room_table')
# def customer_list(request):
#     context = {'customer_list': Customer.objects.all()}
#     return render(request, "customer_table.html", context)
def room_delete(request,id):
    Room.objects.get(Room_ID=id).Room_Image.delete()
    room = Room.objects.get(Room_ID=id)
    room.delete()
    return redirect('room_table')
#booking record
def booking_table(request):
    context={'booking_list':Booking.objects.all()}
    return render(request,'booking_table.html',context)
def bookinginsert(request):
    if request.method == "POST":
        formb=Booking_Form(request.POST,request.FILES)
        formb.save()
        return redirect('room')
    else:
        formb=Booking_Form()
    return render(request,"room.html",{'formb':formb})


