import os

from api_test.api_manager.api_assertions import \
    generate_endpoint_by_city_name_or_country, verify_response_code_type, \
    verify_content_type, verify_longitude_matches_with_user_provided_city, \
    verify_latitude_matches_with_user_provided_city, \
    generate_endpoint_by_zipcode_or_country
from api_test.resources.constants.constant import base_url
from utils.api_functions import ApiHelper
from utils import parser
from os.path import dirname, abspath
import pytest

params = parser.parse_json(os.path.join(
    os.path.join(dirname(dirname(abspath(__file__))), 'resources'),
    'test_city_weather.json'),
    ['city_name', 'country_code', 'latitude', 'longitude'])


@pytest.mark.parametrize('city_name,country_code,latitude,longitude', params)
def test_verify_response_for_city_and_country(city_name, country_code,
                                              latitude, longitude):
    api = ApiHelper()
    complete_url = generate_endpoint_by_city_name_or_country(base_url,
                                                             city_name,
                                                             country_code)
    response_data = api.get(complete_url)
    print(response_data)
    verify_response_code_type(response_data, 200,
                              'API call for city or country code '
                              'api failed for input ' + city_name + ','
                              + country_code)
    verify_content_type(response_data, 'application/json',
                        'Response type is not application/json')
    verify_longitude_matches_with_user_provided_city(response_data,
                                                     longitude,
                                                     'Longitude value '
                                                     'from api response for '
                                                     + city_name +
                                                     ' is invalid')
    verify_latitude_matches_with_user_provided_city(response_data, latitude,
                                                    'Longitude value from api'
                                                    ' response for '
                                                    + city_name +
                                                    ' is invalid')


params = parser.parse_json(os.path.join(
    os.path.join(dirname(dirname(abspath(__file__))), 'resources'),
    'test_zipcode_weather.json'),
    ['zip_code', 'country_code'])


@pytest.mark.parametrize('zip_code,country_code', params)
def test_verify_response_for_zipcode_and_country(zip_code, country_code):
    api = ApiHelper()
    complete_url = generate_endpoint_by_zipcode_or_country(base_url,
                                                           zip_code,
                                                           country_code)
    response_data = api.get(complete_url)
    print(response_data)
    verify_response_code_type(response_data, 200,
                              'API call for city or country code '
                              'api failed for input ' + str(zip_code) + ','
                              + country_code)
    verify_content_type(response_data, 'application/json',
                        'Response type is not application/json')
