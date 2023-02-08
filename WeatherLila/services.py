import requests


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_weather_info(params={}):
    coordinates = get_coordinates()
    url = 'https://api.openweathermap.org/data/2.5/onecall?' + coordinates[0] + '&' + coordinates[1] + \
          '&exclude=minutely&units=metric&appid=e7704bc895b4a8d2dfd4a29d404285b6'

    response = generate_request(url, params)
    if response:
        return response


def get_coordinates():
    with open('coordinates.txt') as file:
        lines = file.readlines()
        lines[0] = lines[0].replace('\n', '')
        return lines
