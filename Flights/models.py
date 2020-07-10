from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

#Flight Model
class Flight(models.Model):
    Departure = models.CharField(max_length=20)
    Arrival = models.CharField(max_length=20)
    FlightDate = models.DateTimeField()
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(default='default.jpg', upload_to='destination_pics')
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.Arrival}'

#Reservation Model
class Reservation(models.Model):
    users = models.ManyToManyField(User)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Flight.Arrival}'




