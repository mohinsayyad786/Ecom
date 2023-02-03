from django.contrib import admin
from django.urls import path
from ecomapp import views

urlpatterns = [
    path('',views.index),
    path('hom',views.homes),
    path('pro',views.product),
    path('add',views.add_product),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('register',views.Register),
    path('login',views.Login),
    path('logout',views.Logout),
    path('getid',views.getlogonuserid),


]