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
from my_booking_app.views import views,customerview,roomview,bookingview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #for admin page
    #for loading pages
    path('', views.index, name="index page"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('help/', views.help, name="help"),
    path('room/', roomview.room, name="room"),
    path('privacy/', views.privacy, name="privacy"),
    path('adminpage/', views.admin, name="admin_page"),
    path('logout/',views.logout,name="logout"),
    #for customer
    path("dashboard/'<int:id>'", customerview.customerdashboard),
    path("customer_edit/<int:id>/", customerview.customer_edit, name="customeredit"),
    path("customer_update/<int:id>", customerview.customer_update, name="customerupdate"),
    path('customer_delete/<int:id>/', customerview.customer_delete, name='customer_delete'),
    path('customer_register/', customerview.customersignup, name="customersignup"),
    path('loginValidate/', customerview.loginValidate, name="customerlogin"),
    path('adminpage/customer_record/', customerview.customer_table, name="customer_table"),
    path('adminpage/customersearch', customerview.customersearch, name='customersearch'),
    #for booking
    path('booking/', bookingview.bookinginsert, name="bookinginsert"),
    path('adminpage/booking_record/', bookingview.booking_table, name="booking_table"),
    #for room
    path('adminpage/room_record/', roomview.room_table, name="room_table"),
    path('adminpage/room_insert', roomview.roominsert, name='room_insert'),
    path('adminpage/room_edit/<int:id>/', roomview.room_edit, name='room_update'),
    path('adminpage/room_update/<int:id>/', roomview.room_update, name='room_finally_update'),
    path('adminpage/room_delete/<int:id>/', roomview.room_delete, name='room_delete'),
    # booking

    # path('adminpage/booking_insert', views.bookinginsert, name='booking_insert'),
    # path('adminpage/booking_edit/<int:id>/', views.booking_edit, name='booking_update'),
    # path('adminpage/booking_update/<int:id>/', views.booking_update, name='booking_finally_update'),# get and post req. for update operation
    # path('adminpage/booking_delete/<int:id>/', views.booking_delete, name='booking_delete'),
    # path('adminpage/customer_list/', views.customer_list, name='customer_list')
]
urlpatterns += staticfiles_urlpatterns()
