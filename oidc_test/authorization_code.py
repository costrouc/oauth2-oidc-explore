import time
import webbrowser
import urllib.parse
import http.server
import socketserver

import requests


# https://www.oauth.com/oauth2-servers/authorization/the-authorization-request/
def flow(oidc_endpoint_configuration: str, client_id: str, client_secret: str, state: str):
    oidc_config = requests.get(oidc_endpoint_configuration).json()

    done = False
    id_token = None
    access_token = None
    refresh_token = None
    start_time = time.time()

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            nonlocal done
            nonlocal id_token
            nonlocal access_token
            nonlocal refresh_token
            query = urllib.parse.parse_qs(urllib.parse.urlparse(self.requestline.split()[1]).query)
            code = query['code'][0]
            request_state = query['state'][0]

            assert request_state == state

            response = requests.post(
                oidc_config["token_endpoint"],
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": "http://localhost:8000/callback",
                    "client_id": client_id,
                    "client_secret": client_secret,
                },
            )
            response.raise_for_status()
            data = response.json()
            refresh_token = data["refresh_token"]
            access_token = data["access_token"]
            id_token = data["id_token"]

            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write("Done. You can close browser".encode("utf-8"))
            done = True

    qs = urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": "http://localhost:8000/callback",
            "scope": "openid",
            "state": state,
        }
    )
    webbrowser.open(f"{oidc_config['authorization_endpoint']}?{qs}")

    with socketserver.TCPServer(("", 8000), Handler) as httpd:
        while not done:
            if time.time() - start_time > 60:
                print("callback timeout")
                break
            httpd.handle_request()    

    return id_token, access_token, refresh_token
    
    
