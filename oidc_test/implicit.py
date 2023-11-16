import time
import webbrowser
import urllib.parse
import http.server
import socketserver

import requests


# https://curity.io/resources/learn/oauth-implicit-flow/
def flow(oidc_endpoint_configuration: str, client_id: str, state: str):
    oidc_config = requests.get(oidc_endpoint_configuration).json()

    done = False
    access_token = None
    start_time = time.time()

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            nonlocal done
            nonlocal access_token
            
            if "?" not in self.requestline:
                # A trick to convert /callback#... to /callback?... 
                # this is becuase #... cannot be captured by the server
                self.send_response(200, "OK")
                self.headers.add_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write("""
<script>
window.location.href = "http://localhost:8000?" + window.location.hash.substring(1)
</script>            
""".encode('utf-8'))
            else:
                # capture the query
                query = urllib.parse.parse_qs(urllib.parse.urlparse(self.requestline.split()[1]).query)
                access_token = query['access_token'][0]
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(b"Done. Trick to extract implicit achortag information to server")
                done = True

    qs = urllib.parse.urlencode(
        {
            "response_type": "token",
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

    return access_token
    
    
