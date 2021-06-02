from django.shortcuts import render, redirect

from .models import *
from django.http import HttpResponseNotFound, HttpResponse


def go_booking_page(request):
    cities = Rooms.objects.all()

    context = {
        'cities': cities,


    }
    return render(request, 'index.html', context)


def room_page(request, pk):
    if int(pk) > 3:
        return redirect('index', permanent=True)

    name = reserve_rooms[pk]['name']
    context = {
        'name': name
    }
    print(pk)

    return render(request, 'reserve/booking_page.html', context)


def show_room(request, room_id):
    return HttpResponse(f'Hello gnida{room_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,'
                                '<strong>долбаеб</strong></h1>')
