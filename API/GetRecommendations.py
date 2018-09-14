#!/usr/bin/env python

"""
    This should return recommend locations based on select locations
"""

import google_places

def GetRecommendations(params):
    googleAPI = google_places.google_places()
    data = googleAPI.get_data_on_place(params["name"])
    if data is None:
        return {"success" : False, "msg" : "Failed getting google api data"}

    return {"success":True, "locations" : data}