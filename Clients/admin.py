from django.contrib import admin
from .models import Client,Reservation,Flight


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('FirstName', 'LastName', 'Email', 'BirthDate', 'MobileNumber', 'Gender')


@admin.register(Reservation)
class ClientAdmin(admin.ModelAdmin):
    fields = ('clients', 'Flight')


@admin.register(Flight)
class ClientAdmin(admin.ModelAdmin):
    fields = ('Departure', 'Arrival', 'FlightDate')