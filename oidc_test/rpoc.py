import requests
import jwt


# https://auth0.com/docs/get-started/authentication-and-authorization-flow/resource-owner-password-flow
def flow(oidc_endpoint_configuration: str, client_id: str, client_secret: str, username: str, password: str):
    oidc_config = requests.get(oidc_endpoint_configuration).json()
    
    response = requests.post(
        oidc_config["token_endpoint"],
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "username": username,
            "password": password,
            "grant_type": "password",
        },
    )
    response.raise_for_status()

    data = response.json()
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]

    # validate the access token
    jwks_client = jwt.PyJWKClient(oidc_config["jwks_uri"])
    signing_key = jwks_client.get_signing_key_from_jwt(access_token)
    jwt.decode(
        access_token, key=signing_key.key, algorithms=["RS256"],
    )
    return access_token, refresh_token
