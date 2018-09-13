from googleAPI import *
from googlemaps import client 

SEARCH_KEY_WORD = "things to do"

class google_places(object):
    """docstring for ClassName"""
    def __init__(self):
        super(ClassName, self).__init__()
        self.client = client.Client(key="AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s")
        
    def get_initial_places(self, dates, place)
        places_result = places(client = self.client, query = , radius = radius, open_now = True)