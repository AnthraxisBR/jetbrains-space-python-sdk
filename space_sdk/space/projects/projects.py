from ..space import Space


class Projects(Space):
    project: str

    def __init__(self, project=None):
        urn: str = '/projects/key:{}/'

        super(Projects, self).__init__()

        self.project: str = project

        self.urn += urn
