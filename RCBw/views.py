from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainWindow(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/RCB'> Link to registration page</a> <br> <h2> TAATAAA BYEEEE BYEEEE<h2>")