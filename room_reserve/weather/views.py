from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from weather.forms import WeatherForm
from .services import *


@login_required
def index(request):
    form = WeatherForm()
    result = ''

    if request.method == 'POST':
        selected_city = request.POST['city_field']

        result += what_weather(selected_city)

    context = {
        'title': 'Weather',
        'form': form,
        'weather': result
    }
    print(result)
    return render(request, 'weather/index.html', context)
