from rest_framework import serializers

from .models import Events

class EventsJson(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'content')