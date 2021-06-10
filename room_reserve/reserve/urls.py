from .views import *
from django.urls import path

from .views import pageNotFound


urlpatterns = [
    path('main/', index, name='index'),
    path('booking/<int:reserver_id>/', reserve_room, name='reception'),
]

handler404 = pageNotFound
