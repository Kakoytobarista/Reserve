from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name='index'),
    path('booking/', views.go_booking_page, name='booking')
]
