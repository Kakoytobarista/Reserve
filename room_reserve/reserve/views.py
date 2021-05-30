from django.shortcuts import render, redirect
from .models import reserve_rooms
from django.http import HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def go_booking_page(request):
    rooms = ''

    for i in range(len(reserve_rooms)):
        booking_form = f'<a href="booking/{i}/">{reserve_rooms[i]["name"]}</a><br>'

        rooms += booking_form

    context = {
        'rooms': rooms

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


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Слушай брат, нахуй ты сюда зашел, иди на правильный редирект,<strong>долбаеб</strong></h1>')
