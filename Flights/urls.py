from django.urls import path,include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Flights'

urlpatterns = [
    # Home views
    path('', views.Home_view, name='Home'),
    url('Flights', views.Flights_View, name='Flights'),
    url('flights_filter/', views.Flights_filter, name='Flightsfilter'),
    url('dislike/', views.dislike, name='dislike'),
    url('like/', views.like, name='like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
