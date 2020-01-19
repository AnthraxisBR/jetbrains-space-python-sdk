from ..space import Space


class Absence(Space):
    project: str

    def __init__(self, absence=None):
        urn: str = '/absences/'

        super(Absence, self).__init__()

        self.absence: str = absence

        self.urn += urn

g