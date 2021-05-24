from django.shortcuts import render
from .models import reserve_rooms


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
    name = reserve_rooms[pk]['name']
    context = {
        'name': name
    }
    return render(request, 'reserve/booking_page.html', context)

