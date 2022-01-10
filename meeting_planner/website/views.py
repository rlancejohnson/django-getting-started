from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(response):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")