from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('host',views.host,name='host'),
    path('join',views.join,name='join'),
    path('login',views.login,name='loginpage'),
]
