from django.shortcuts import render
from .models import Flight, Reservation
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.dateparse import parse_date
# import the logging library
import logging
from django.core.serializers import serialize

# Get an instance of a logger
logger = logging.getLogger(__name__)

def Home_view(request):
    Flights = Flight.objects.all()
    return render(request,'Flight/list.html')

def Flights_View(request):
    Flights = Flight.objects.all()
    paginator = Paginator(Flights, 6)
    page_number = request.GET.get('page')
    if (page_number == None):
        page_obj =paginator.get_page(1)
    else:
        page_obj = paginator.get_page(page_number)
    return render(request,'Flight/Flights.html',{'Flights_pg':page_obj})


def Flights_filter(request):
    if request.method == 'POST':
        current_place = request.POST['current_place']
        destination = request.POST['destination']
        daterange = request.POST['daterange']
        price_range = request.POST['price_range']
        sdate1= daterange[6:10] + "-" + daterange[:2] + "-" + daterange[3:5]
        sdate2= daterange[19:23] + "-" + daterange[13:15] + "-" + daterange[16:18]
        Flights = Flight.objects.filter(Departure__icontains=current_place,Arrival__icontains=destination,Price__lte=price_range,FlightDate__range=(sdate1,sdate2))
        paginator = Paginator(Flights, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_obj_json=serialize('json', page_obj)
        return JsonResponse({'Flights_pg':page_obj_json})
    else:
        return render(request, 'Flight/Flights.html')

def like(request):
    Flight_id=request.GET.get('flightid')
    current_Flight = Flight.objects.get(pk=Flight_id)
    current_Flight.likes.add(request.user)
    current_Flight.save()
    return JsonResponse({'msg':'Liked successfully'})

def dislike(request):
    Flight_id=request.GET.get('flightid')
    current_Flight = Flight.objects.get(pk=Flight_id)
    current_Flight.likes.remove(request.user)
    current_Flight.save()
    return JsonResponse({'msg':'Disliked successfully'})
    

