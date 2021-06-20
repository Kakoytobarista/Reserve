from .views import *
from django.urls import path

from .views import pageNotFound


urlpatterns = [
    path('main/', MainPage.as_view(), name='index'),
    path('booking/<slug:reserver_slug>/', DetailRoom.as_view(), name='detail'),
    path('booking/', AddReserve.as_view(), name='reserving'),
    path('feedback/', ContactFormView.as_view(), name='feedback')
]

handler404 = pageNotFound
