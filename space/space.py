from client.base import Client


class Space(Client):
    urn: str = '/api/http'

    def __init__(self):
        super(Space, self).__init__()

    def mount_base_path(self, urn: str) -> str:
        self.urn += urn
        return self.urn
