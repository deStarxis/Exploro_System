"""Booking_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#importing all the views
from my_booking_app.views import views,customerview,roomview,bookingview
#importing url patterns for static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    #for admin page
    #for index page
    path('', views.index, name="index page"),
    path('index/', views.index, name="index"),
    #for about us page
    path('about/', views.about, name="about"),
    #for room page
    path('room/', roomview.room, name="room"),
    #for privacy policy page
    path('privacy/', views.privacy, name="privacy"),
    #for admin dashboard
    path('adminpage/', views.admin, name="admin_page"),
    #for logging out from the admin dashboard
    path('logout/',views.logout,name="logout"),

    #for customer
    #for customer dashboard
    path("dashboard/'<int:id>'", customerview.customerdashboard),
    #for customer edit
    path("customer_edit/<int:id>/", customerview.customer_edit, name="customeredit"),
    #for updating the customer
    path("customer_update/<int:id>", customerview.customer_update, name="customerupdate"),
    #for deletion of the customer
    path('customer_delete/<int:id>/', customerview.customer_delete, name='customer_delete'),
    #for signup form
    path('customer_register/', customerview.customersignup, name="customersignup"),
    #for login form for the customer
    path('loginValidate/', customerview.loginValidate, name="customerlogin"),
    #for customer record in the admin dashboard
    path('adminpage/customer_record/', customerview.customer_table, name="customer_table"),

    #for booking
    #for booking form in room page
    path('booking/', bookingview.bookinginsert, name="bookinginsert"),
    #for booking record in the admin dashboard
    path('adminpage/booking_record/', bookingview.booking_table, name="booking_table"),
    #for deleting the booking record in admin dashboard
    path('adminpage/booking_delete/<int:id>/',bookingview.booking_delete,name='booking_delete'),

    #for room
    #for inserting new room in the database
    path('adminpage/room_insert', roomview.roominsert, name='room_insert'),
    #for editing the room details
    path('adminpage/room_edit/<int:id>/', roomview.room_edit, name='room_update'),
    #for updating the room details
    path('adminpage/room_update/<int:id>/', roomview.room_update, name='room_finally_update'),
    #for deleting the room details
    path('adminpage/room_delete/<int:id>/', roomview.room_delete, name='room_delete'),
    #for viewing the room record in admin dashboard
    path('adminpage/room_record/', roomview.room_table, name="room_table"),
]
#for static files like images
urlpatterns += staticfiles_urlpatterns()
