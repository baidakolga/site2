from django.forms import  ModelForm
from .models import Events

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('title', 'content', 'period')




