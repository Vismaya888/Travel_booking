from django.contrib import admin
from .models import Destination,Flight,Booking

# Register your models here.

admin.site.register(Destination)
admin.site.register(Flight)
admin.site.register(Booking)
