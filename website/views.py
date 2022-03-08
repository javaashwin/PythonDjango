from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

from meetings.models import Meeting,Room

def welcome(request):
    return render(request,"website/welcome.html",
                  {"message":"This is a demo dynamic message",
                   "message1":"This is a templete example",
                   "meetings":Meeting.objects.all(),
                   })


def date(request):
    return HttpResponse("this page was served at" +str(datetime.now()))

def about(request):
    return HttpResponse("I am Ashwin working at accenture as a fresher")