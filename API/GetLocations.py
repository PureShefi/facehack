#!/usr/bin/env python

"""
    This function should return popular locations based on a city
"""

import google_places

def GetLocations(params):
    if "city" not in params.keys():
        return {"success" : False, "locations": [], "msg" : "Invalid params, missing city"}

    try:
        googleAPI = google_places.google_places()
        data = googleAPI.get_initial_places("1/1/2017", params["city"][0])
        if data is None:
            return {"success" : False, "locations": [], "msg" : "Failed getting google api data"}
    except:
        return {"success" : False, "locations": [], "msg" : "Failed getting google api data, crashed"}

    return {"success": True, "locations": data}