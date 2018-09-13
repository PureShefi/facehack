from googleAPI import *
from googlemaps import client 

location = "London"
query_temp = "resturants in london"
radius = "1000"
client_temp = client.Client(key="AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s")
places_result = places(client = client_temp, query = query_temp, radius = radius, open_now = True)
print(places_result["results"]) 