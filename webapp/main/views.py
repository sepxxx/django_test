from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>CHECK UP</h4>")

def about(request):
    return HttpResponse("<h4>ABOUT US</h4>")
