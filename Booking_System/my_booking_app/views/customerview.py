from django.db.models import Q
from django.shortcuts import render, redirect
#importing authentication
from my_booking_app.authenticate import Authenticate
#importing customer form
from my_booking_app.forms.customerform import Customer_Signup_Form
#importing customer model
from my_booking_app.models.customermodel import Customer
from django.contrib import messages

#for customer dashboard
@Authenticate.valid_user
def customerdashboard(request, id):
    context = {'customers': Customer.objects.get(ID=id)}
    return render(request, 'customer_dashboard.html', context)

#for editing details of a particular customer
@Authenticate.valid_user
def customer_edit(request, id):
    customer = Customer.objects.get(ID=id)
    return render(request, 'customer_edit.html', {'customer': customer})

#for updating the customer details
@Authenticate.valid_user
def customer_update(request, id):
    customers = Customer.objects.get(ID=id)
    form = Customer_Signup_Form(request.POST, instance=customers)
    form.save()
    return redirect("/dashboard/'" + str(id) + "'")

#for deleting the customer's account
@Authenticate.valid_user
def customer_delete(request, id):
    customer = Customer.objects.get(ID=id)
    customer.delete()
    return redirect('index page')

#for creating a new customer's account
def customersignup(request):
    if request.method == "POST":
        formc = Customer_Signup_Form(request.POST, request.FILES)
        formc.save()
        return redirect("/index")
    else:
        formc = Customer_Signup_Form()
    return render(request, "index.html", {'formc': formc})

#for viewing customer record in admin dashboard
def customer_table(request):
    if "next" in request.POST:
        context = {'customer_list': Customer.objects.raw("select * from customer limit 10 offset 10")}
    else:
        context = {'customer_list': Customer.objects.raw("select * from customer limit 10 offset 0")}
    return render(request, "customer_table.html", context)

#for validating the login of customer and admin
def loginValidate(request):
    try:
        #storing email and password in session
        request.session['Email'] = request.POST["Email"]
        request.session['Password'] = request.POST["Password"]
        #admin login
        if (request.session['Email'] == "admin@gmail.com"):
            if (request.session['Password'] == "admin123"):
                return redirect('/adminpage/')
        else:
        #customer login
            customers = Customer.objects.get(Q(Email=request.session['Email']) & Q(Password=request.session['Password']))
            id = customers.ID
            return redirect("/dashboard/'" + str(id) + "'")
    except:
        messages.warning(request,"Invalid Username or Password")
        return redirect('/index/')


