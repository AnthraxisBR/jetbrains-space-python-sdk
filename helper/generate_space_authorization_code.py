import urllib
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler


from lib.oauth2.oauth2 import SpaceOauth2

SCOPE='**'

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><code>{message}</code></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        self._set_headers()
        args = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(self.path).query))
        oauth = SpaceOauth2(
            redirect_uri='http://localhost:8000/callback',
            client_id=os.getenv('SPACE_CLIENT_ID'),
            scope=SCOPE)

        if 'code' in args:
            response_str: str = oauth.get_access_token_from_code(args['code'], 'http://localhost:8000/callback').decode('utf-8')
            response: dict = json.loads(response_str)
            print('Access Token: ' + response['access_token'])

            self.wfile.write(self._html(response_str))
            exit()
        elif 'access_token' in self.path:
            print(self.path.split('#')[1])
            exit()
        else:
            print(oauth.get_access_token_from_client_credentials(SCOPE))
            exit()

    def do_HEAD(self):
        self._set_headers()



def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    oauth = SpaceOauth2(
        redirect_uri='http://localhost:8000/callback',
        client_id=os.getenv('SPACE_CLIENT_ID'),
        scope=SCOPE
    )

    #print(oauth.get_access_token_from_client_credentials('**'))
    print('Abra o link a baixo em um navegador: ')
    print(oauth.get_code_url())
    print(f"Aguardando autenticação {addr}:{port}")
    httpd.serve_forever()

run()


