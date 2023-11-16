import keycloak


class Keycloak:
    def __init__(self, server_url: str = "http://localhost:8080", username: str = "admin", password: str = "password"):
        self.connection = keycloak.KeycloakOpenIDConnection(
            server_url=server_url,
            username=username,
            password=password,
            realm_name="master",
        )
        self.client = keycloak.KeycloakAdmin(connection=self.connection)

    def create_realm(self, realm: str, skip_exists: bool = False):
        self.client.change_current_realm("master")
        self.client.create_realm(payload={"realm": realm}, skip_exists=skip_exists)

    def delete_realm(self, realm: str):
        self.client.change_current_realm("master")
        self.client.delete_realm(realm)

    def create_user(self, realm: str, email: str, username: str, password: str, skip_exists: bool = False):
        self.client.change_current_realm(realm)
        # https://www.keycloak.org/docs-api/22.0.1/rest-api/index.html#UserRepresentation        
        self.client.create_user(payload={
            "email": email,
            "username": username,
            "enabled": True,
            "emailVerified": True,
            "credentials": [{"value": password,"type": "password",}]
        }, exist_ok=skip_exists)

    def create_group(self, realm: str, name: str, skip_exists: bool = False):
        self.client.change_current_realm(realm)
        self.client.create_group(payload={"name": name}, skip_exists=skip_exists)

    def create_client(self, realm: str, client_id: str, client_secret: str, name: str, callback_urls: list[str], skip_exists: bool = False):
        self.client.change_current_realm(realm)
        # https://www.keycloak.org/docs-api/22.0.1/rest-api/index.html#ClientRepresentation 
        self.client.create_client(payload={
            "clientId": client_id,
            "name": name,
            "redirectUris": callback_urls,
            "secret": client_secret,
            "publicClient": False,
            "consentRequired": False,
            "standardFlowEnabled": True,       # grant: authorization_code
            "implicitFlowEnabled": True,       # grant: implicit
            "directAccessGrantsEnabled": True, # grant: resource owner password credentials (rpoc)
            "serviceAccountsEnabled": True,    # grant: client credentials
        }, skip_exists=skip_exists)


def seed_realm(client: Keycloak, realm: str, users: list[str], groups: list[str], clients: list[str]):
    client.create_realm(realm, skip_exists=True)
    
    for user in users:
        client.create_user(realm, email=f"{user}@example.com", username=user, password="password", skip_exists=True)

    for group in groups:
        client.create_group(realm, group, skip_exists=True)

    for _client in clients:
        client.create_client(realm, client_id=_client, client_secret=_client, name=_client, callback_urls=["http://localhost:8000/callback"], skip_exists=True)


