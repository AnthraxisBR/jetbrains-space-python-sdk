import settings
import os
import requests
import base64
from urllib import parse


class SpaceOauth2(object):
    url: str

    urn: str = '/oauth/auth'

    response_type: str = 'code'

    state: str

    redirect_uri: str

    request_credentials: str = 'skip'

    client_id: str

    scope: str = '**'

    def __init__(self,
                 response_type: str = 'code',
                 state: str = '',
                 redirect_uri: str = '',
                 request_credentials: str = '',
                 client_id: str = '',
                 scope: str = '**'
                 ):
        self.url = os.getenv('SPACE_HOST')
        self.response_type = response_type
        self.state = state
        self.redirect_uri = redirect_uri
        self.request_credentials = request_credentials
        self.client_id = client_id
        self.scope = scope

    def get_base64_secrets(self):
        concat: str = os.getenv('SPACE_CLIENT_ID') + ':' + os.getenv('SPACE_CLIENT_SECRET')
        encoded: str = base64.b64encode(concat.encode('utf-8')).decode('utf-8')
        return encoded

    def get_code_url(self) -> str:
        url: str = self.url + self.urn + '?'
        params: dict = {
            'response_type': self.response_type,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'client_id': os.getenv('SPACE_CLIENT_ID')
        }
        url += parse.urlencode(params)
        return url

    def get_access_token_from_code(self, code: str, redirect_uri: str):
        """
            grant_type=authorization_code&code=${Code received on a previous step}&redirect_uri=${Client redirect URI}
        :param scope:
        :return:
        """
        params: dict = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
        }
        headers: dict = {
            'Authorization': 'Basic ' + self.get_base64_secrets(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': os.getenv('SPACE_HOST'),
            'Accept': 'application/json'
        }
        url: str = self.url + '/oauth/token'
        response = requests.post(url, data=params, headers=headers)
        content = response.content

        return content
