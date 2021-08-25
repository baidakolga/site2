from django.shortcuts import render, HttpResponse, redirect
#from django.http import JsonResponse
from .models import Events
#from .serializers import EventsJson
from .forms import EventForm

import time


def childhood(request):  # request - obaviazkova
    data = Events.objects.filter(period__name='Childhood')
    return render(request, 'life/childhood.html', {"data": data})


def youth(request):
    data = Events.objects.filter(period__name='Youth')
    return render(request, 'life/youth.html', {"data": data})

def adult(request):
    data = Events.objects.filter(period__name='Adult')
    return render(request, 'life/adult.html', {"data": data})

def senility(request):
    data = Events.objects.filter(period__name='Senility')
    return render(request, 'life/senility.html', {"data": data})




def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/add_event/')
    return render(request, 'life/add_event.html', {'form': EventForm()})



#def my_api(request):
   # data_from_db = Events.objects.all()
    #some_data =  EventsJson(data_from_db, many = True)
   # return JsonResponse(some_data.data, safe = False)