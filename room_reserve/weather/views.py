from django.shortcuts import render

from weather.forms import WeatherForm
from .services import *


def index(request):
    form = WeatherForm()
    result = ''

    if request.method == 'POST':
        selected_city = request.POST

        result += what_weather(selected_city)

    context = {
        'title': 'Weather',
        'form': form,
        'weather': result
    }
    print(result)
    return render(request, 'weather/index.html', context)
