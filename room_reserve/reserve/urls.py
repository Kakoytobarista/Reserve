from django.urls import path
from . import views
from .views import pageNotFound

urlpatterns = [
    path('main/', views.go_booking_page, name='index'),
    path('main/booking/<int:room_id>/', views.show_room, name='room')
]

handler404 = pageNotFound
