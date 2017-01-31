# Author : Michael Hawes
# Project Leo
# weather.py

import json
import urllib.request
from subprocess import call

"""
most of this code came from http://codereview.stackexchange.com/questions/131371/script-to-print-weather-report-from-openweathermap-api
"""
class Weather:

    def get_weather(self):

        print('success')
        user_api = 'e0505ad0c414329d4dae5fc6f31e7be9'  # Obtain yours form: http://openweathermap.org/
        unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
        api = 'http://api.openweathermap.org/data/2.5/weather?id='     # Search for your city ID here: http://bulk.openweathermap.org/sample/city.list.json.gz

        full_api_url = api + str(4779999) + '&mode=json&units=' + unit + '&APPID=' + user_api

        url = urllib.request.urlopen(full_api_url)
        output = url.read().decode('utf-8')
        raw_api_dict = json.loads(output)
        url.close()

        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        cloudiness=raw_api_dict.get('clouds').get('all')


        m_symbol = '\xb0' + 'Farenheight'

        call(["espeak", "-v", "mb-us1", 'Current weather in:' + str(city)])
        #print('Current weather in: {}, {}:'.format(data['city'], data['country']))
        call(["espeak", "-v", "mb-us1", 'It is' + str(temp) + str(m_symbol)])
        #print('It is',data['temp'], m_symbol)
        call(["espeak", "-v", "mb-us1", 'Today there will be a high of:' + str(temp_max) + "degrees" + "and a low of:" + str(temp_min) + "degrees"])
        #print('Today there will be a high of: {}, and a low of: {}'.format(data['temp_max'], data['temp_min']))
        call(["espeak", "-v", "mb-us1", 'Wind Speed is currently:' + str(wind) + "miles per hour"])
        #print('Wind Speed is currently: {}'.format(data['wind'], 'mph'))
