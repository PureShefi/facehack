from googleAPI import *
from googlemaps import client 

SEARCH_KEY_WORD = "best things to do"
RADIUS          = 10000
API_KEY         = "AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s"
WANTED_VALUES   = (u'rating', u'name',u'geometry',u'photos')

class google_places(object):
    """
        Handels the google places operations.
    """
    def __init__(self):
        super(google_places, self).__init__()
        self.client = client.Client(key=API_KEY)
        
    """
        this function get the initial places, give it a place and it returns a dict with the WANTED VALUES details. 
    """
    def get_initial_places(self, dates, place):
        output_list = []
        query_to_search = SEARCH_KEY_WORD+" in "+place
        places_result = places(client = self.client, query = query_to_search , radius = RADIUS)
        results_list = places_result.get(u'results')
        for result in results_list:
            output_dict = {}
            try:
                data_dict = places_result.get(u'results').pop()
            except IndexError:
                return "failed"
            for detail in WANTED_VALUES:
                output_dict[detail] = data_dict[detail] 
            output_list.append(output_dict)
        return output_list
