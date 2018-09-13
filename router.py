#!/usr/bin/env python

from API.GetLocations import GetLocations
from API.GetEvents import GetEvents
from API.GetRecommendations import GetRecommendations

class Router():
    """
        A class which gets a route string and and function and 
        calls the function when needed
    """
    def __init__(self, baseFunction):
        self.routes = {}
        self.baseFunction = baseFunction

    def Insert(self, route, function):
        self.routes[route.lower()] = function

    def __getitem__(self, key):
        key = key.lower()
        if key not in self.routes.keys():
            print "Damn"
            return self.baseFunction

        return self.routes[key]

"""
    Functions for the routing
"""
def Base(dict):
    return {"success" : False}

"""
    Initialize the router with needed functions
"""
urlRouter = Router(Base)
urlRouter.Insert("/", Base)
urlRouter.Insert("/events", GetEvents)
urlRouter.Insert("/locations", GetLocations)
urlRouter.Insert("/recommendation", GetRecommendations)