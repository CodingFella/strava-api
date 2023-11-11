# stravawrapper/__init__.py

import os
import requests

STRAVA_API_KEY = os.environ.get('STRAVA_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if STRAVA_API_KEY is None:
    raise APIKeyMissingError(
        "Access Token is required to run. "
        "Visit https://www.strava.com/settings/api to find yours. "
        "Once you find it, run again with STRAVA_API_KEY=YOUR_CODE_HERE py.test"
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = STRAVA_API_KEY

from .api import API