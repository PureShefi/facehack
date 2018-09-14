#!/usr/bin/python
from weather import Weather, Unit
from enum import Enum
import datetime

class WeatherStatus(Enum):
    FAIR = 0
    GENERAL_BAD = 1
    LIGHT_RAIN = 2
    HEAVY_RAIN = 3
    LIGHT_SNOW = 4
    HEAVY_SNOW = 5
    DANGEROUS = 6
    UNKOWN = 7

class WeatherForecast():
    def __init__(self):
        self.weather = Weather(unit=Unit.CELSIUS)

    def GetForecast(self, location, startDate, endDate):
        """
            Return a forecasts containing
            text - textual representation of the weather
            date - the date
            high - highest temp on date
            low - lowest temp on date
            code - yahoo forecast code to ours
            weather - our weather code
        """

        location = self.weather.lookup_by_location(location)
        forecastList = []
        for forecast in location.forecast:
            date = datetime.datetime.strptime(forecast.date, '%d %b %Y')
            if not startDate <= date <= endDate:
                continue

            forecastList.append({'code':forecast.code,  'date':forecast.date,  'day':forecast.day,  'high':forecast.high,  'low':forecast.low,  'text':forecast.text })

        return forecastList

    def IsFair(self, forecast):
        status = self.YahooForcastToOurForecast(forecast)
        return status == WeatherStatus.FAIR or status == WeatherStatus.GENERAL_BAD or status == WeatherStatus.LIGHT_RAIN or status == WeatherStatus.UNKOWN

    def YahooForcastToOurForecast(self, yahooCode):
        return {
            "0":      WeatherStatus.DANGEROUS, # "tornado",
            "1":      WeatherStatus.DANGEROUS, # tropical storm
            "2":      WeatherStatus.DANGEROUS, # hurricane
            "3":      WeatherStatus.DANGEROUS, # severe thunderstorms
            "4":      WeatherStatus.HEAVY_RAIN, # thunderstorms
            "5":      WeatherStatus.HEAVY_RAIN, # mixed rain and snow
            "6":      WeatherStatus.HEAVY_RAIN, # mixed rain and sleet
            "7":      WeatherStatus.HEAVY_RAIN, # mixed snow and sleet
            "8":      WeatherStatus.HEAVY_RAIN, # freezing drizzle
            "9":      WeatherStatus.LIGHT_RAIN, # drizzle
            "10":     WeatherStatus.HEAVY_RAIN, # freezing rain
            "11":     WeatherStatus.HEAVY_RAIN, # showers
            "12":     WeatherStatus.HEAVY_RAIN, # showers
            "13":     WeatherStatus.HEAVY_SNOW, # snow flurries
            "14":     WeatherStatus.HEAVY_SNOW, # light snow showers
            "15":     WeatherStatus.HEAVY_SNOW, # blowing snow
            "16":     WeatherStatus.HEAVY_SNOW, # snow
            "17":     WeatherStatus.HEAVY_SNOW, # hail
            "18":     WeatherStatus.HEAVY_SNOW, # sleet
            "19":     WeatherStatus.GENERAL_BAD, # dust
            "20":     WeatherStatus.GENERAL_BAD, # foggy
            "21":     WeatherStatus.GENERAL_BAD, # haze
            "22":     WeatherStatus.GENERAL_BAD, # smoky
            "23":     WeatherStatus.FAIR, # blustery
            "24":     WeatherStatus.FAIR, # windy
            "25":     WeatherStatus.FAIR, # cold
            "26":     WeatherStatus.FAIR, # cloudy
            "27":     WeatherStatus.FAIR, # mostly cloudy (night)
            "28":     WeatherStatus.FAIR, # mostly cloudy (day)
            "29":     WeatherStatus.FAIR, # partly cloudy (night)
            "30":     WeatherStatus.FAIR, # partly cloudy (day)
            "31":     WeatherStatus.FAIR, # clear (night)
            "32":     WeatherStatus.FAIR, # sunny
            "33":     WeatherStatus.FAIR, # fair (night)
            "34":     WeatherStatus.FAIR, # fair (day)
            "35":     WeatherStatus.HEAVY_RAIN, # mixed rain and hail
            "36":     WeatherStatus.FAIR, # hot
            "37":     WeatherStatus.HEAVY_RAIN, # isolated thunderstorms
            "38":     WeatherStatus.LIGHT_RAIN, # scattered thunderstorms
            "39":     WeatherStatus.LIGHT_RAIN, # scattered thunderstorms
            "40":     WeatherStatus.LIGHT_RAIN, # scattered showers
            "41":     WeatherStatus.HEAVY_SNOW, # heavy snow
            "42":     WeatherStatus.LIGHT_SNOW, # scattered snow showers
            "43":     WeatherStatus.HEAVY_SNOW, # heavy snow
            "44":     WeatherStatus.FAIR, # partly cloudy
            "45":     WeatherStatus.HEAVY_RAIN, # thundershowers
            "46":     WeatherStatus.HEAVY_SNOW, # snow showers
            "47":     WeatherStatus.HEAVY_RAIN, # isolated thundershowers
            "3200":   WeatherStatus.UNKOWN, # not available
        }.get(str(yahooCode), WeatherStatus.UNKOWN) 