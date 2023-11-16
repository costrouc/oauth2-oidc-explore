import grpc
import bcrypt

from oidc_test.dex import api_pb2_grpc, api_pb2


class Dex:
    def __init__(self, server_url: str = "localhost:5557"):
        self.channel = grpc.insecure_channel(server_url)
        self.stub = api_pb2_grpc.DexStub(self.channel)

    def create_user(self, email: str, username: str, password: str, skip_exists: bool = False):
        response: api_pb2.CreatePasswordResp = self.stub.CreatePassword(api_pb2.CreatePasswordReq(
            password=api_pb2.Password(
                email=email,
                hash=bcrypt.hashpw(b"password", bcrypt.gensalt()),
                username=username,
                user_id=username,    
            )
        ))
        if response.already_exists and not skip_exists:
            raise ValueError(f"email {email} already exists")

    def create_client(self, client_id: str, client_secret: str, callback_urls: list[str], skip_exists: bool = False):
        response: api_pb2.CreateClientResp = self.stub.CreateClient(
            api_pb2.CreateClientReq(
                client=api_pb2.Client(
                    id=client_id,
                    name=client_id,
                    secret=client_secret,
                    redirect_uris=callback_urls,
                    public=False,
                )
            )
        )
        if response.already_exists and not skip_exists:
            raise ValueError(f'client {client_id} already exists')


def seed(client: Dex, users: list[str], clients: list[str]):
    for user in users:
        client.create_user(email=f"{user}@example.com", username=user, password="password", skip_exists=True)

    for _client in clients:
        client.create_client(client_id=_client, client_secret=_client, callback_urls=["http://localhost:8000/callback"], skip_exists=True)        


