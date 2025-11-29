# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color: red;'>Homepage</h1>")

def room(request):
    return HttpResponse("<h1 style='color: blue;'>Room</h1>")
