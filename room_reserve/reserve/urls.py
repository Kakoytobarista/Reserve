from .views import *
from django.urls import path

from .views import pageNotFound


urlpatterns = [
    path('main/', index, name='index'),
    path('main/booking/<int:reserver_id>/', ReceptionView.as_view(), name='reception'),
]

handler404 = pageNotFound
