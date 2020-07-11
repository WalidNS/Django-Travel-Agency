from django.urls import path,include
from . import views as v
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Authentification'

urlpatterns = [
    path('signup/', v.signup, name='signup'),
    path('login/', v.login, name='login'),
    path('logout/', v.logout, name='logout'),
]

