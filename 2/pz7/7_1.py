import json
import requests
import sys
import bs4


def get_weather_json(location, api_key):
    url = (f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&mode=json&appid'
           f'={api_key}')
    response = requests.get(url)
    response.raise_for_status()
    forecasts = json.loads(response.text)['list']
    uniques = set()
    weather_data = list()
    for forecast in forecasts:
        time = forecast['dt_txt'][:10]
        weather_description = forecast['weather'][0]['description']
        temperature = forecast['main']['temp']
        if time not in uniques:
            data_point = {
                'time': time,
                'weather_description': weather_description,
                'temperature': temperature,
            }
            weather_data.append(data_point)
            uniques.add(time)
    return weather_data


def get_weather_xml(location, api_key):
    url = (f'https://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&mode=xml&appid'
           f'={api_key}')
    response = requests.get(url)
    response.raise_for_status()
    weather_xml = bs4.BeautifulSoup(response.text, features="xml")
    forecasts = weather_xml.select('time')
    uniques = set()
    weather_data = list()
    for forecast in forecasts:
        time = forecast['from'][:10]
        weather_description = forecast.find('symbol')['name']
        temperature = forecast.find('temperature')['value']
        if time not in uniques:
            data_point = {
                'time': time,
                'weather_description': weather_description,
                'temperature': temperature,
            }
            weather_data.append(data_point)
            uniques.add(time)
    return weather_data


def print_weather_info(location, weather_info):
    print(f'Current weather in {location}:')
    print(f'Date: {weather_info[0]["time"]}, temperature: {weather_info[0]["temperature"]},'
          f' weather: {weather_info[0]["weather_description"]}.')
    print()
    print('Tomorrow:')
    print(f'Date: {weather_info[1]["time"]}, temperature: {weather_info[1]["temperature"]},'
          f' weather: {weather_info[1]["weather_description"]}.')
    print()
    print('Day after tomorrow:')
    print(f'Date: {weather_info[2]["time"]}, temperature: {weather_info[2]["temperature"]},'
          f' weather: {weather_info[2]["weather_description"]}.')
    print('==========================================================================================')


if len(sys.argv) < 2:
    print('Usage: 7_1.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
api_key = 'bbe41e835eb32586e588d6d1adec8acc'


xml_weather_info = get_weather_xml(location, api_key)
json_weather_info = get_weather_json(location, api_key)
print_weather_info(location, json_weather_info)
print_weather_info(location, xml_weather_info)
