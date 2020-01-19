from ..space import Space


class Administration(Space):
    project: str

    def __init__(self, administration=None):
        urn: str = '/administration'

        super(Administration, self).__init__()

        self.administration: str = administration

        self.urn += urn