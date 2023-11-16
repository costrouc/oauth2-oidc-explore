import uuid

from oidc_test import authorization_code
from oidc_test.dex import client

client.seed(client.Dex('localhost:5557'), users=["chris"], clients=['testclient'])


id_token, access_token, refresh_token = authorization_code.flow(
    oidc_endpoint_configuration="http://localhost:5556/dex/.well-known/openid-configuration",
    client_id="testclient",
    client_secret="testclient",
    state=uuid.uuid4().hex,
)
print(id_token, access_token, refresh_token)
