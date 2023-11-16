import uuid

from oidc_test import authorization_code

id_token, access_token = authorization_code.flow(
    oidc_endpoint_configuration="http://localhost:5556/dex/.well-known/openid-configuration",
    client_id="testclient",
    client_secret="uFvSYbkVXvtBIoqX0OB4Ot8aU3OztiUE",
    state=uuid.uuid4().hex,
)
print(id_token, access_token)
