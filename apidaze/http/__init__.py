from enum import Enum
import requests


class HttpMethodEnum(Enum):
    GET = "get"
    POST = "post"
    DELETE = "delete"


class Http(object):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        self.base_url = 'https://api4.apidaze.io/' + api_key

    def request(
            self,
            method: HttpMethodEnum,
            endpoint: str,
            payload: dict,
            headers: dict = {},
            params: dict = {}):
        if not isinstance(method, Enum):
            raise TypeError(
                'method must be an instance of HttpMethodEnum Enum')

        params = {'api_secret': self.api_secret}

        # TODO: use an URL parser to join
        url = self.base_url + endpoint
        headers = self.getHeadersWithDefault(headers=headers)
        response = None

        if params:
            params.update(params)

        if method == HttpMethodEnum.POST:
            response = requests.post(
                url, params=params, headers=headers, data=payload)
        elif method == HttpMethodEnum.GET:
            response = requests.get(
                url, params=params, headers=headers, data=payload)
        elif method == HttpMethodEnum.DELETE:
            response = requests.delete(url, params=params, headers=headers)

        return response

    def getHeadersWithDefault(self, headers={}):
        default = {
            'content-type': 'application/x-www-form-urlencoded'
        }

        default.update(headers)

        return default
