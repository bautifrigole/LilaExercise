import sys
from services import get_weather_info
from datetime import date, datetime


weekdays = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}


def get_min_max_temperature():
    return list(map(lambda x: [x.get('temp').get('min'), x.get('temp').get('max')],
                    get_weather_info().get('daily')))


def show_min_max_temperature():
    print("Min and max temperature for the next 5 days: ")
    day_index = date.today().weekday()
    temp_days_info = get_min_max_temperature()
    for i in range(6):
        print(weekdays[day_index % 7] + " |  min: " + str(temp_days_info[i][0])
              + "°C, max:" + str(temp_days_info[i][1]) + "°C")
        day_index += 1


if len(sys.argv) > 1 and sys.argv[1] == "-min_max_temperature":
    show_min_max_temperature()


def get_rain_info_next_hours():
    return list(map(lambda x: x.get('pop'), get_weather_info().get('hourly')))


def show_rain_info_next_hours():
    print("Probability of precipitation in the next 24 hours: ")
    hour = datetime.now().hour
    rain_hours_info = get_rain_info_next_hours()
    for i in range(24):
        print(str(hour % 24) + ":00 |  Probability of precipitation: " + str(rain_hours_info[i]))
        hour += 1


if len(sys.argv) > 1 and sys.argv[1] == "-rain_info_next_hours":
    show_rain_info_next_hours()


def get_highest_rain_day():
    rain_info_days = list(map(lambda x: x.get('pop'), get_weather_info().get('daily')))
    return [rain_info_days.index(max(rain_info_days)), max(rain_info_days)]


def show_highest_rain_day():
    print("The day with the highest probability of precipitation of the next 7 days is: ")
    today_index = date.today().weekday()
    day_info = get_highest_rain_day()
    print(weekdays[(today_index + day_info[0]) % 7] + " | Probability of precipitation: " + str(day_info[1]))


if len(sys.argv) > 1 and sys.argv[1] == "-highest_rain_day":
    show_highest_rain_day()
