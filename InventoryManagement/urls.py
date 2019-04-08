"""InventoryManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path , include
#from django.contrib.auth.views import login

from inventory.views import home_view, login_view, inventory_add_view, inventory_fetch_view, inventory_approve_view,inventory_change_view,inventory_change_record_view,inventory_delete_record_view

urlpatterns = [

    path('admin/', admin.site.urls ,  name = 'admin'),

    path('home/', home_view ,  name = 'home_view'),
    path('accounts/' , include('django.contrib.auth.urls') ),

    path('imsys/',login_view, name='login_view'),

    
    path('inventory/allrecords/', inventory_change_view, name='inventory_change_view'),
    path('inventory/add/', inventory_add_view, name='inventory_add_view'),
    path('inventory/change/<int:id>/', inventory_change_record_view, name='inventory_change_record_view'),
    path('inventory/delete/<int:id>/', inventory_delete_record_view, name='inventory_delete_record_view'),


    path('inventory/fetch/', inventory_fetch_view, name='inventory_fetch_view'),
    path('inventory/<int:id>/', inventory_approve_view, name='inventory_approve_view'),
]
