import requests
import jwt

OIDC_ENDPOINT_CONFIGURATION = (
    "http://localhost:8080/realms/develop/.well-known/openid-configuration"
)
CLIENT_ID = "testclient"
CLIENT_SECRET = "uFvSYbkVXvtBIoqX0OB4Ot8aU3OztiUE"

oidc_config = requests.get(OIDC_ENDPOINT_CONFIGURATION).json()

print(oidc_config["authorization_endpoint"])
print(oidc_config["token_endpoint"])
print(oidc_config["userinfo_endpoint"])


# https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-client-credentials-flow
response = requests.post(
    oidc_config["token_endpoint"],
    data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "audience": "testclient",
        "grant_type": "client_credentials",
    },
)
response.raise_for_status()

data = response.json()
access_token = data["access_token"]
print("got access client credentials token!")

# validate the access token
jwks_client = jwt.PyJWKClient(oidc_config["jwks_uri"])
signing_key = jwks_client.get_signing_key_from_jwt(access_token)
token = jwt.decode(
    access_token, key=signing_key.key, algorithms=["RS256"], audience="account"
)
print(token)
