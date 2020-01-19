from ..space import Space


class AuthModules(Space):
    project: str

    def __init__(self, auth_modules=None):
        urn: str = '/auth-modules'

        super(AuthModules, self).__init__()

        self.auth_modules: str = auth_modules

        self.urn += urn
