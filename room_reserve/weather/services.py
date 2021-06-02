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

    if response.status_code == 200:
        return response.text

    else:
        return f'try again later'
