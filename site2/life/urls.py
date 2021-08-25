from django.urls import path
from .views import childhood, youth, senility, adult, add_event

urlpatterns = [
    path('', childhood),
    path('youth/', youth),
    path('adult/', adult),
    path('senility/', senility),
    path('add_event/', add_event),
    path('events/',add_event),
    ]
