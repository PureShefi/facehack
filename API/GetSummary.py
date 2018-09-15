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

def BadWeatherDaysCount(forecasts):
    """
        Checks if there is a bad weather during the trip
        if so counts how many
    """
    badWeatherDays = 0

    for forecast in forecasts:
        if not weatherForecast.IsFair(forecast["code"]):
            badWeatherDays += 1

    return badWeatherDays


def GroupLocationsByDistance(locations, days):
    """
        Groups locations together to be as closest as possible to each other
    """
    locs = ClusterLocations(locations)

    return NormalizeLocations(locs, days)

def NormalizeLocations(locations, days):
    """
        Break/Merge the groups if there arent or too many groups
        in a single day
    """

    # TODO: later filter and merge groups based on location time
    if days <= 1:
        return locations

    if len(locations) == days:
        return locations

    # If length is too short, break up large days
    while len(locations) < days:
        listLength = len(max(locations))

        # make sure each cluster is larger than 3
        if listLength <= 3:
            break

        for loc in locations:
            # Split largest location in half
            currListLength = len(loc)
            if listLength == currListLength:
                locations.remove(loc)
                locations.append(loc[:currListLength/2])
                locations.append(loc[currListLength/2:])
                break

    # if length is too large, append together the smallest lists
    while len(locations) > days:
        smallest = min(locations)
        locations.remove(smallest)

        secondSmallest = min(locations)
        locations.remove(secondSmallest)

        locations.append(smallest + secondSmallest)

    return locations

def ClusterCenter(locations):
    """
        return the center of all the locations
        (lat, long)
    """
    latitude = sum([loc["latitude"] for loc in locations])
    longitude = sum([loc["longitude"] for loc in locations])

    arrLen = len(locations)
    return {"latidude" :latitude/arrLen, "longitude":longitude/arrLen}


def GetClosest(locations, center):
    """
        return the closest location to the center, and its distance
        returns (location, distance)
    """
    minDist = 10000000 # Large number that will always be larger than smallest distance
    closest = locations[0]

    for loc in locations:
        dist = sqrt((loc["latitude"] - center["latitude"])**2 + (loc["longitude"] - center["longitude"])**2)
        if dist < minDist:
            minDist = dist
            closest = loc

    return (closest, minDist)

def SmartAdd(indoor, outdoor):
    """
        Gets a single indoor and outdoor cluster
        returns the closest location which distance is smaller then the threshhold
    """
    threshhold = 1 #
    center = ClusterCenter(outdoor)
    closest, distance = GetClosest(indoor)

    if distance < threshhold:
        indoor.remove(closest)
        outdoor.add(closest)
        return True

    return False


def NormalizeIndoorOutdoor(indoor, outdoor):
    """
        Validate that there aren't too many things to do on indoor days
        and not enough on outdoor
    """
    # TODO: Here lies the big money, so make this better! Add ML and blockchain, those always work

    # outdoor days are long enough
    if len(min(outdoor)) >= 3:
        return

    # indoor days are short enough
    if len(max(indoor)) <= 3:
        return

    # If there is an indoor day twice as 
    for outLoc in outdoor:

        # out loc is large enough
        if  len(max(indoor)) / 2 < len(outLoc):
            continue

        # TODO: not that effecient but who cares right now
        indoor.sort().reverse()
        success = False

        for loc in indoor:
            if len(loc) < len(outLoc):
                return

            # all the items are too short
            if len(loc) <= 3:
                return

            # if succeeded adding try again
            if SmartAdd(indoor, outLoc):
                success = True
                break

        # if all failed passing threshold, then break to stop infinte loop
        if not success:
            return

def GetSummary(params):
    weather = MockWeatherWeek()
    locations = MockLocations()
    days = len(weather)
    badWeatherDays = BadWeatherDaysCount(weather)

    locGroups = []
    # check weather we should break the objects to indoors and outdoors
    if badWeatherDays == 0:
        locGroups = GroupLocationsByDistance(locations, days)
    else:
        indoor, outdoor = GroupLocationByWeatherLimits(locations)
        indoor = GroupLocationsByDistance(indoor, badWeatherDays)
        outdoor = GroupLocationsByDistance(outdoor, days - badWeatherDays)
        NormalizeIndoorOutdoor(indoor, outdoor)
        locGroups = indoor + outdoor


    return {"success":True, "weather": weather, "locations": locGroups}
