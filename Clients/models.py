from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Client(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    BirthDate = models.DateField()
    Mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Wrong Phone number")
    MobileNumber = models.CharField(validators=[Mobile_regex], max_length=17, unique=True, blank=True)
    Gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    Gender = models.CharField(
        max_length=20,
        choices=Gender_choices,
        default="M",
    )

    created = models.DateTimeField(auto_now_add=True)


class Flight(models.Model):
    Departure = models.CharField(max_length=20)
    Arrival = models.CharField(max_length=20)
    FlightDate = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):
    clients = models.ManyToManyField(Client)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)




