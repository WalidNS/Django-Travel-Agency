from django.urls import path,include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Flights'

urlpatterns = [
    # Home views
    path('', views.Home_view, name='Home'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
