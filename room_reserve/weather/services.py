import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }

    try:
        response = requests.get(url, params=weather_parameters)

    except requests.ConnectionError:
        return 'Try again later, network fail'

    while int() not in response:
        return response.text.strip()
