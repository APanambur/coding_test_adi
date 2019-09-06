import allure

from api_test.resources.constants.constant import API_key


@allure.step("Generating endpoint for city & country for "
             "retrieving weather details")
def generate_endpoint_by_city_name_or_country(base_url, city_name,
                                              country_code):
    """
    function to generate end points for city & country based on parameters
    :param base_url: Base url of openweather api
    :param city_name: City name value
    :param country_code: Country code value
    :return: base_url: Newly constructed api endpoint
    """
    if city_name and not country_code:
        base_url = base_url + 'APPID=' + API_key + '&q=' + city_name
    elif not city_name and country_code:
        base_url = base_url + 'APPID=' + API_key + '&q=' + country_code
    elif city_name and country_code:
        base_url = base_url + 'APPID=' + API_key + '&q=' + city_name + ',' + \
                   country_code
    else:
        base_url = "NA"
    return base_url


@allure.step("Generating endpoint for zipcode & country for "
             "retrieving weather details")
def generate_endpoint_by_zipcode_or_country(base_url, zip_code,
                                            country_code):
    """
    function to generate end points for zipcode & country based on parameters
    :param base_url: Base url of openweather api
    :param zip_code: Zip code value
    :param country_code: Country code value
    :return: base_url: Newly constructed api endpoint
    """
    if zip_code and not country_code:
        base_url = base_url + 'APPID=' + API_key + '&zip=' + str(zip_code)
    elif not zip_code and country_code:
        base_url = base_url + 'APPID=' + API_key + '&zip=' + country_code
    elif zip_code and country_code:
        base_url = base_url + 'APPID=' + API_key + '&zip=' + str(
            zip_code) + ',' + \
                   country_code
    else:
        base_url = "NA"
    return base_url


@allure.step("Verify response code for the response")
def verify_response_code_type(response, expected_response_code, err_msg):
    """
    function to verify response code value
    :param response: Response json value
    :param expected_response_code: Expected response code
    :param err_msg: Error message for failure
    """
    assert response['response'] == expected_response_code, err_msg


@allure.step("Verify response header content type for the response")
def verify_content_type(response, expected_content_type, err_msg):
    """
    function to verify response code value
    :param response: Response json value
    :param expected_content_type: Expected content code
    :param err_msg: Error message for failure
    """
    assert expected_content_type in \
           response['raw_response'].headers['Content-Type'], err_msg


@allure.step("Verify longitude val of response matches with user provide city")
def verify_longitude_matches_with_user_provided_city(response,
                                                     expected_long_val,
                                                     err_msg):
    """
    function to verify longitude code value from response with user provided
     data
    :param response: Response json value
    :param expected_long_val: Expected longitude code
    :param err_msg: Error message for failure
    """
    assert response['json_response']['coord']['lon'] == expected_long_val, \
        err_msg


@allure.step("Verify latitude val of response matches with user provide city")
def verify_latitude_matches_with_user_provided_city(response,
                                                    expected_lat_val,
                                                    err_msg):
    """
    function to verify latitude code value from response with user provided
     data
    :param response: Response json value
    :param expected_lat_val: Expected latitude code
    :param err_msg: Error message for failure
    """
    assert response['json_response']['coord']['lat'] == expected_lat_val, \
        err_msg
