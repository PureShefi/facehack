#!/usr/bin/env python

"""
    A class which gets a route string and and function and 
    calls the function when needed
"""
def BaseFunction(dict):
    return {"error":"yes"}

class Router():
    def __init__(self, baseFunction = BaseFunction):
        self.routes = {}
        self.baseFunction = BaseFunction

    def Insert(self, route, function):
        self.routes[route.lower()] = function

    def __getitem__(self, key):
        key = key.lower()
        if key not in self.routes.keys():
            return self.baseFunction

        return self.routes[key]

"""
    Functions for the routing
"""
def Test(dict):
    return {"Test":"asd"}

def Locations(dict):
    return {"Locations":"asd"}

def Base(dict):
    return {"Base":"asd"}

"""
    Initialize the router with needed functions
"""
urlRouter = Router()
urlRouter.Insert("/", Base)
urlRouter.Insert("/test", Test)
urlRouter.Insert("/locations", Locations)