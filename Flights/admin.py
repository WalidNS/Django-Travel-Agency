from django.contrib import admin
from .models import Reservation,Flight


#Adding flight to admin
@admin.register(Flight)
class ClientAdmin(admin.ModelAdmin):
    fields = ('Departure', 'Arrival', 'FlightDate')

#Adding reservation to admin
@admin.register(Reservation)
class ClientAdmin(admin.ModelAdmin):
    fields = ('clients', 'Flight')