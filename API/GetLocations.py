#!/usr/bin/env python

"""
    This function should return popular locations based on a city
"""

import google_places

LOW_PRICE = 15
MEDIUM_PRICE = 30
def PriceCalculator(price):
    """
        Calculates how many dollars the price is
        0  -       free
        0  -> 15 - $
        15 -> 30 - $$
        30 -> .. - $$$

    """
    if price == 0:
        return "free"

    if price <= LOW_PRICE:
        return "$"

    if price <= MEDIUM_PRICE:
        return "$$"

    return "$$$"

def MockLocations():
    """
        Mock locations for test
    """
    locs = {"locations" :
            [
                {"name": "Statue of liberity", "img" : "www.google.com", "description" : "This is a fucking large statue", "price" : PriceCalculator(25)},
                {"name": "Centeral Park", "img" : "www.google.com", "description" : "Large park in the middle of manahatan", "price" : PriceCalculator(0)},
            ]}

    return locs

def GetLocations(params):
    if "city" not in params.keys():
        return {"success" : False, "msg" : "Invalid params, missing city"}

    try:
        googleAPI = google_places.google_places()
        data = googleAPI.get_initial_places("1/1/2017", params["city"][0])
        if data is None:
            return {"success" : False, "msg" : "Failed getting google api data"}
    except:
        return {"success" : False, "msg" : "Failed getting google api data, crashed"}

    return {"success": True, "locations": data}