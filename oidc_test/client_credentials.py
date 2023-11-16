import requests
import jwt


# https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-client-credentials-flow
def flow(oidc_endpoint_configuration: str, client_id: str, client_secret: str):
    oidc_config = requests.get(oidc_endpoint_configuration).json()
    
    response = requests.post(
        oidc_config["token_endpoint"],
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "audience": "testclient",
            "grant_type": "client_credentials",
        },
    )
    response.raise_for_status()

    data = response.json()
    access_token = data["access_token"]

    # validate the access token
    jwks_client = jwt.PyJWKClient(oidc_config["jwks_uri"])
    signing_key = jwks_client.get_signing_key_from_jwt(access_token)
    jwt.decode(
        access_token, key=signing_key.key, algorithms=["RS256"],
    )
    return access_token
