# stravawrapper/test_api.py

from pytest import fixture
from stravawrapper import API
import vcr

@fixture
def athlete_keys():
    return ['id']

@vcr.use_cassette('tests/vcr_cassettes/api-athlete.yml', filter_query_parameters=['api_key'])
def test_api_info(athlete_keys):
    """Tests an API call to get an athlete"""

    api_instance = API()
    response = api_instance.athlete()
    
    assert isinstance(response, dict)
    assert isinstance(response['id'], int)
