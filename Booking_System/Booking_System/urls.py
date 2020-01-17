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
from my_booking_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index page"),
    path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('help/',views.help,name="help"),
    path('room/',views.room,name="room"),
    path('privacy/',views.privacy,name="privacy"),
    # path('customer_login/',views.),
    # path('customer_entry/',views.customer_entry,name="customerentry"),
    path('customer_register/',views.customersignup,name="customersignup"),
    path('adminpage/',views.admin,name="admin_page"),
    #customer
    path('adminpage/customer_record/',views.customer_table,name="customer_table"),
    # path('adminpage/customer_insert', views.customerinsert, name='customer_insert'),
    # path('adminpage/customer_edit/<int:id>/', views.customer_edit, name='customer_update'),
    # path('adminpage/customer_update/<int:id>/', views.customer_update, name='customer_finally_update'),# get and post req. for update operation
    # path('adminpage/customer_delete/<int:id>/', views.customer_delete, name='customer_delete'),
    path('adminpage/customersearch', views.customersearch,name='customersearch'),
    #room
    path('adminpage/room_record/',views.room_table,name="room_table"),
    path('adminpage/room_insert', views.roominsert, name='room_insert'),
    path('adminpage/room_edit/<int:id>/', views.room_edit, name='room_update'),
    path('adminpage/room_update/<int:id>/', views.room_update, name='room_finally_update'),# get and post req. for update operation
    path('adminpage/room_delete/<int:id>/', views.room_delete, name='room_delete'),
    #booking
    path('adminpage/booking_record/',views.booking_table,name="booking_table"),
    # path('adminpage/booking_insert', views.bookinginsert, name='booking_insert'),
    # path('adminpage/booking_edit/<int:id>/', views.booking_edit, name='booking_update'),
    # path('adminpage/booking_update/<int:id>/', views.booking_update, name='booking_finally_update'),# get and post req. for update operation
    # path('adminpage/booking_delete/<int:id>/', views.booking_delete, name='booking_delete'),
    # path('adminpage/customer_list/', views.customer_list, name='customer_list')
]
urlpatterns+=staticfiles_urlpatterns()
