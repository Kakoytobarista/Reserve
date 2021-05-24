from django.urls import path
from . import views

urlpatterns = [
    # path('main/', views.index, name='index'),
    path('main/', views.go_booking_page, name='index'),
    path('main/booking/<int:pk>/', views.room_page)
]
