class Revision(object):
    repository: str

    commit: str

    def __init__(self, repository: str, commit: str):
        self.repository = repository
        self.commit = repository

    def __todict__(self):
        return {
            'repository': self.repository,
            'commit': self.commit
        }


class Revisions(object):
    revisions: list

    def append_revision(self, revision: Revision):
        self.revisions.append(revision)

    def all_revisions(self):
        revisions: list = []
        for revision in self.revisions:
            revisions.append(revision.__todict__())
        return revisions

    def __todict__(self):
        return {
            'revisions': self.all_revisions()
        }
