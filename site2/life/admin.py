from django.contrib import admin

from .models import Events, Period

# Register your models here.

admin.site.register(Events)
admin.site.register(Period)