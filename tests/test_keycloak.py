import uuid

from oidc_test import authorization_code, keycloak, client_credentials, rpoc, implicit

realm = "testrealm"
client = "testclient"
keycloak.seed_realm(
    keycloak.Keycloak(),
    realm,
    users=["chris"],
    groups=["datascience"],
    clients=[client],
)

# id_token, access_token, refresh_token = authorization_code.flow(
#     oidc_endpoint_configuration=f"http://localhost:8080/realms/{realm}/.well-known/openid-configuration",
#     client_id=client,
#     client_secret=client,
#     state=uuid.uuid4().hex,
# )
# print('authorization_code', id_token, access_token, refresh_token)


# access_token = client_credentials.flow(
#     oidc_endpoint_configuration=f"http://localhost:8080/realms/{realm}/.well-known/openid-configuration",
#     client_id=client,
#     client_secret=client,
# )
# print('client_credentials', access_token)


# access_token, refresh_token = rpoc.flow(
#     oidc_endpoint_configuration=f"http://localhost:8080/realms/{realm}/.well-known/openid-configuration",
#     client_id=client,
#     client_secret=client,
#     username="chris",
#     password="password",
# )
# print('resource owner password credentials', access_token, refresh_token)


access_token, refresh_token = implicit.flow(
    oidc_endpoint_configuration=f"http://localhost:8080/realms/{realm}/.well-known/openid-configuration",
    client_id=client,
    state=uuid.uuid4().hex,
)
print('implicit', access_token, refresh_token)