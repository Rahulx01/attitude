from asyncio import constants
from cgitb import text
from datetime import datetime
import email
from importlib.resources import contents
from multiprocessing import context
from traceback import print_tb
from unicodedata import name
from django import http
from django.shortcuts import render,HttpResponse
from home.models import Host
# Create your views here.
def index(request):
    return render(request,'index.html')

def host(request):
    if(request.method == "POST"):
        email = request.POST.get('email')
        password = request.POST.get('password')
        hostevent = Host(email = email,password = password)
        hostevent.save()
    return render(request,'host.html')

def join(request):
    allevents = Host.objects.all()
    context = {'events' : allevents}
    # for ele in allevents:
    #     print(ele.password)
    return render(request,'join.html',context)

def login(request):
    return render(request,'login.html')
    if request.method == "POST":
        print(5)
