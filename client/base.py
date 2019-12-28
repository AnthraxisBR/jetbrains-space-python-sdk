import urllib

import requests


class Client(object):

    url: str

    headers: dict

    def __init__(self, url: str = ''):
        self.url = url

    def set_headers(self, headers: dict) -> None:
        self.headers = headers

    def __build_url(self, urn: str = '', params=None) -> str:
        if params is None:
            params = {}
        url: str = self.url + urn
        if params and params is not None:
            url += '?' + urllib.parse.urlencode(params)
        return url

    def get(self, urn: str, params=None):
        try:
            response = requests.get(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response.content
        except:
            return False

    def delete(self, urn: str, params=None):
        try:
            response = requests.delete(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response.content
        except:
            return False

    def post(self, urn: str, data=None, params=None):
        try:
            response = requests.post(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            return response.content
        except:
            return False

    def patch(self, urn: str, data=None, params=None):
        try:
            response = requests.patch(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            return response.content
        except:
            return False

    def put(self, urn: str, data=None, params=None):
        try:
            response = requests.patch(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            return response.content
        except:
            return False
