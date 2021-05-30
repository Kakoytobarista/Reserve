from django.urls import path

from weather.views import *

urlpatterns = [
    path('weather/', index, name='weather_page')
]


