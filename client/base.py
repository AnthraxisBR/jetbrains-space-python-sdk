import settings
import os
import urllib
import requests


class Client(object):

    url: str

    headers: dict

    def __init__(self, url: str = ''):
        self.url = url

        self.set_headers({
            'Authorization': 'Bearer ' + os.getenv('SPACE_ACCESS_TOKEN'),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def set_headers(self, headers: dict) -> None:
        self.headers = headers

    def __build_url(self, urn: str = '', params=None) -> str:
        if params is None:
            params = {}
        url: str = os.getenv('SPACE_API_HOST') + self.url + urn
        if params and params is not None:
            url += '?' + urllib.parse.urlencode(params)
        return url

    def get(self, urn: str, params=None):
        try:
            print(self.__build_url(urn=urn, params=params))
            response = requests.get(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response
        except Exception as e:
            print(e)
            return False

    def delete(self, urn: str, params=None):
        try:
            response = requests.delete(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response
        except Exception as e:
            print(e)
            return False

    def post(self, urn: str, data=None, params=None, json=None):
        try:
            if data is None and json is not None:
                response = requests.post(self.__build_url(urn=urn, params=params), json=json, headers=self.headers)
            elif json is None and data is not None:
                response = requests.post(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            else:
                response = requests.post(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response
        except Exception as e:
            print(e)
            return False

    def patch(self, urn: str, data=None, params=None, json=None):
        try:
            if data is None and json is not None:
                response = requests.patch(self.__build_url(urn=urn, params=params), json=json, headers=self.headers)
            elif json is None and data is not None:
                response = requests.patch(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            else:
                response = requests.patch(self.__build_url(urn=urn, params=params), headers=self.headers)
            return response
        except Exception as e:
            print(e)
            return False

    def put(self, urn: str, data=None, params=None):
        try:
            response = requests.patch(self.__build_url(urn=urn, params=params), data=data, headers=self.headers)
            return response
        except:
            return False
