from googleAPI import *
from googlemaps import client 

SEARCH_KEY_WORD        = "best things to do"
RADIUS                 = 10000
API_KEY                = "AIzaSyAtVGYjp7gGHRu0YcoRAxyB_IruztcMx1s"
WANTED_VALUES          = (u'rating', u'name',u'geometry',u'photos', u'types')
USER_SEARCH_INPUT_TYPE = "textquery" 

class google_places(object):
    """
        Handels the google places operations.
    """
    def __init__(self):
        super(google_places, self).__init__()
        self.client = client.Client(key=API_KEY)
    """
        filter the data in a dictionary.
    """
    def _get_desired_data(self, result):
        output_dict = {}
        for detail in WANTED_VALUES:
            output_dict[detail] = result[detail]
        return output_dict

    """
        this function get the initial places, give it a place and it returns a dict with the WANTED VALUES details. 
    """
    def get_initial_places(self, dates, place):
        output_list = []
        query_to_search = SEARCH_KEY_WORD+" in "+place
        places_result = places(client = self.client, query = query_to_search , radius = RADIUS)
        results_list = places_result.get(u'results')
        for result in results_list:
            output = self._get_desired_data(result = result)
            output_list.append(output)
        return output_list


    """
        get the data of a desired place.
    """
    def get_data_on_place(self, in_query):
        output_list = []
        find_place_result = find_place(client = self.client, input = in_query, input_type = USER_SEARCH_INPUT_TYPE)

        try:
            places_result = place(client = self.client, place_id = find_place_result.get(u'candidates').pop().get(u'place_id'))
        except IndexError as x:
            print x
            return []

        result = places_result.get(u'result')
        if(result == None):
            return output_list
        output = self._get_desired_data(result = result)
        output_list.append(output)
        return output_list 


