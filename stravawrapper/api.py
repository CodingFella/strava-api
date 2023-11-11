# stravawrapper/api.py

from . import session


class API(object):
    def __init__(self):
        pass
    
    def athlete(self):
        headers = {'Authorization': 'Bearer ' + session.params['api_key']}
        path = "https://www.strava.com/api/v3/athlete"
        response = session.get(path, headers=headers)
        return response.json()