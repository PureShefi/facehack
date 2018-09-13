#!/usr/bin/env python

"""
    This should return recommend locations based on select locations
"""
def GetRecommendations(params):
    if "city" not in params.keys():
        return {"success":False, "act":"recommend"}

    return {"success":True, "act":"recommend"}