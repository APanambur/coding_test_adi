from urllib.error import URLError

import requests
from requests import HTTPError

from utils.logger import custom_logger


class ApiHelper:

    def __init__(self):
        self.log = custom_logger()

    def get(self, url, headers={}):
        "Get request"
        json_response = None
        error = {}
        try:
            response = requests.get(url=url, headers=headers)
            try:
                json_response = response.json()
            except:
                json_response = None
        except (HTTPError, URLError) as e:
            error = e
            self.log.error("GET Error: {}.Error is {}".format(url, e))
        self.log.info("Json response is {}".format(json_response))
        return {'raw_response': response, 'response': response.status_code, 'text': response.text,
                'json_response': json_response, 'error': error}

    def post(self, url, params=None, data=None, json=None, headers={}):
        "Post request"
        error = {}
        json_response = None
        try:
            response = requests.post(url, params=params, json=json,
                                     headers=headers)
            try:
                json_response = response.json()
            except:
                json_response = None
        except (HTTPError, URLError) as e:
            error = e
            self.log.error("POST Error: {} {} {}".format(url, error, str(json)))
        self.log.info("Json response is {}".format(json_response))
        return {'response': response.status_code, 'text': response.text,
                'json_response': json_response, 'error': error}
