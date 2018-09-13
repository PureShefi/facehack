#!/usr/bin/env python

"""
    This function should return popular locations based on a city
"""
def GetLocations(params):
    if "city" not in params.keys():
        return {"success" : False, "act":"locations"}

    return {"success" : True, "act":"locations"}