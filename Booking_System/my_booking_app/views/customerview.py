from django.shortcuts import render, redirect
from my_booking_app.authenticate import Authenticate
from my_booking_app.forms.customerform import Customer_Signup_Form
from my_booking_app.models.customer import Customer
from my_booking_app.models.room import Room
from my_booking_app.models.booking import Booking
from django.http import HttpResponse, JsonResponse
@Authenticate.valid_user
def customerdashboard(request, id):
    context = {'customers': Customer.objects.get(ID=id)}
    # context2 ={'bookings': Booking.objects.get(Booking_ID=id2)}
    return render(request, 'customer_dashboard.html', context)


def customer_edit(request, id):
    customer = Customer.objects.get(ID=id)
    return render(request, 'customer_edit.html', {'customer': customer})

def customer_update(request, id):
    customers = Customer.objects.get(ID=id)
    form = Customer_Signup_Form(request.POST, instance=customers)
    form.save()
    return redirect("/dashboard/'" + str(id) + "'")

def customer_delete(request, id):
    customer = Customer.objects.get(ID=id)
    customer.delete()
    return redirect('index page')
def customersignup(request):
    if request.method == "POST":
        formc = Customer_Signup_Form(request.POST, request.FILES)
        formc.save()
        return redirect("/index")
    else:
        formc = Customer_Signup_Form()
    return render(request, "index.html", {'formc': formc})
def customer_table(request):
    if "next" in request.POST:
        context = {'customer_list': Customer.objects.raw("select * from customer limit 10 offset 10")}
    else:
        context = {'customer_list': Customer.objects.raw("select * from customer limit 10 offset 0")}
    return render(request, "customer_table.html", context)

def loginValidate(request):
    request.session['Email'] = request.POST["Email"]
    request.session['Password'] = request.POST["Password"]
    if (request.session['Email'] == "admin@gmail.com"):
        if (request.session['Password'] == "admin123"):
            return render(request, 'admin.html')
    else:
        customers = Customer.objects.get(Email=request.session['Email'])
        id = customers.ID
        return redirect("/dashboard/'" + str(id) + "'")

def customersearch(request):
    customer = Customer.objects.filter(Email=request.GET['searchbar_customer']).values()
    return JsonResponse(list(customer), safe=False)

