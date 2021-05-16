from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import UpdateView


def index(request):
    return render(request, 'index.html')


def go_booking_page(request):
    return render(request, 'reserve/booking_page.html')
