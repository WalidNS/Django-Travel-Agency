from django.shortcuts import render
from .models import Flight, Reservation
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.password_validation import validate_password
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
# import the logging library
import logging
from django.core.serializers import serialize

# Get an instance of a logger
logger = logging.getLogger(__name__)

def Home_view(request):
    Flights = Flight.objects.all()
    return render(request,'Flight/list.html',{'Flights': Flights})
