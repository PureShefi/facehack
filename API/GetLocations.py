#!/usr/bin/env python

"""
    This function should return popular locations based on a city
"""

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
        return {"success" : False}

    data = MockLocations()
    # data = GoogleLocations.GetLocations(params["city"])
    if data is None:
        return {"success" : False}

    data.update({"success" : True})
    return data