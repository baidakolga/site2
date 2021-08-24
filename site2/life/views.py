from django.shortcuts import render, HttpResponse
from .models import Events
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
