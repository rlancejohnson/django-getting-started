from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html")

def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about(request):
    return HttpResponse(f"I am excited to start writing python django code for Patri.")