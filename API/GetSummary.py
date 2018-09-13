#!/usr/bin/env python

"""
    This should summarize the whole trip and do all the calculation
"""
from weatherAPI import *
from Utils.cluster import ClusterLocations

weatherForecast = WeatherForecast()

def MockWeatherWeek():
    return [
            {"date":"1-1-1990", "code" : 32},
            {"date":"1-2-1990", "code" : 9},
            {"date":"1-3-1990", "code" : 32},
            {"date":"1-4-1990", "code" : 32},
            {"date":"1-5-1990", "code" : 32},
            {"date":"1-6-1990", "code" : 32},
            {"date":"1-7-1990", "code" : 32},
            ]

def MockLocations():
    return [
            {"name":"Big Ben", "lat":37.769006, "long":-122.429299},
            {"name":"Eifal tower", "lat":37.769044, "long":-122.429130},
            {"name":"Jersalem", "lat":37.768775, "long":-122.429092},
            {"name":"Hummus", "lat":37.776299, "long":-122.424249},
            {"name":"Sarona", "lat":37.706265, "long":-122.424657},
            ]
def GroupLocationByWeatherLimits(locations):
    """
        splits the location by indoor/outdoor
        returns (indoor, outdoor)
    """
    indoor = []
    outdoor = []

    for location in locations:
        if location.type in OUTDOOR_LOCATIONS:
            outdoor.append(location)
        else:
            indoor.append(location)

    return indoor, outdoor

def CheckForBadWeather(forecasts):
    """
        Checks if there is a bad weather during the trip
    """
    for forecast in forecasts:
        if not weatherForecast.IsFair(forecast["code"]):
            return False

    return True

def GroupLocationsByDistance(locations):
    """
        Groups locations together to be as closest as possible to each other
    """
    locs = ClusterLocations(locations)

    # TODO: play with the total time it takes for each location so a day wont be too long
    return locs


def GetSummary(params):

    weather = MockWeatherWeek()
    locations = MockLocations()

    locGroups = []
    if CheckForBadWeather(weather):
        locGroups = GroupLocationsByDistance(locations)
    else:
        indoor, outdoor = GroupLocationByWeatherLimits(locations)
        locGroups = GroupLocationsByDistance(indoor) + GroupLocationsByDistance(outdoor)


    return {"success":True, "weather": weather, "locations": locGroups}
