from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from my_booking_app.authenticate import Authenticate


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def privacy(request):
    return render(request, 'privacy.html')

def admin(request):
    return render(request, "admin.html")

def logout(request):
    del request.session['Email']
    return redirect("index")


