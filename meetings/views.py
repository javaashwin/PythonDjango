from django.shortcuts import render ,get_object_or_404,redirect
from  .models import Meeting
# Create your views here.
from meetings.models import Meeting,Room
from django.forms import modelform_factory
from website.views import welcome

def detail(request,id):
    meeting=get_object_or_404(Meeting,pk=id)
    return render(request,"meetings/detail.html",{"meeting":meeting})

def roomview(request):
    return  render(request,"meetings/roompage.html",
                   {"message":"This page shows the room details",
                    "rooms":Room.objects.all(),


                   })

MeetingForm=modelform_factory(Meeting,exclude=[])
def new(request):
    if(request.method=="POST"):
        form= MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form= MeetingForm()
    return render(request,"meetings/new.html",{"form":form})






