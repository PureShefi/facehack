#!/usr/bin/env python

"""
    This function should return popular events in the city during traveling
"""
def GetEvents(params):
    if "city" not in params.keys():
        return {"success":False, "act":"events"}

    return {"success":True, "act":"events"}