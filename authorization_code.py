import webbrowser
import urllib.parse

import requests
import uvicorn
import fastapi

OIDC_ENDPOINT_CONFIGURATION = (
    "http://localhost:8080/realms/develop/.well-known/openid-configuration"
)
CLIENT_ID = "testclient"
CLIENT_SECRET = "uFvSYbkVXvtBIoqX0OB4Ot8aU3OztiUE"

oidc_config = requests.get(OIDC_ENDPOINT_CONFIGURATION).json()

print(oidc_config["authorization_endpoint"])
print(oidc_config["token_endpoint"])
print(oidc_config["userinfo_endpoint"])


app = fastapi.FastAPI()


@app.get("/callback")
def callback_url(state: str, session_state: str, code: str):
    assert state == "asdfasdfasdf"

    response = requests.post(
        oidc_config["token_endpoint"],
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:8000/callback",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    response.raise_for_status()
    data = response.json()
    access_token = data["access_token"]
    print(access_token)
    id_token = data["id_token"]
    print(id_token)

if __name__ == "__main__":
    # https://www.oauth.com/oauth2-servers/authorization/the-authorization-request/
    qs = urllib.parse.urlencode(
        {
            "response_type": "code",
            "client_id": CLIENT_ID,
            "redirect_uri": "http://localhost:8000/callback",
            "scope": "openid",
            "state": "asdfasdfasdf",
        }
    )
    webbrowser.open(f"{oidc_config['authorization_endpoint']}?{qs}")

    uvicorn.run(app, host="0.0.0.0", port=8000)
