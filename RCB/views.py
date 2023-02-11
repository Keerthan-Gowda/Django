from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(Request):
    #return HttpResponse("<h1 style = 'background:yellow'>Hello! all this is my Django app</h1>")
    my_dict = {"insert_me":"Iam coming from SUBFOLDER RCB_DC/Registration_django.html file of RCB"}
    return render(Request,"RCB_DC/Registration_django.html",context=my_dict)
