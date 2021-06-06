import requests
import math


def what_weather(city):
    s_city = f'{city},RU'
    appid = "f27b598f22ab83b2344a1fe57736a2ed"

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = res.json()

        good_weather = u'\U00002600'

        city_id = data['list'][0]['id']

    except Exception as e:
        return str(e)

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        condition = data['weather'][0]['description']
        print(type(condition))
        temperature = math.ceil(data['main']['temp'])
        temp_min = math.ceil(data['main']['temp_min'])
        temp_max = math.ceil(data['main']['temp_max'])

        if condition == 'ясно':
            return f'{good_weather} Temperature: {temperature}, Min Temperature: {temp_min}, Max Temperature: {temp_max}'

        else:

            return f'Temperature: {temperature}, Min Temperature: {temp_min}, Max Temperature: {temp_max}'

    except Exception as e:
        return str(e)
