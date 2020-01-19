



class TD_ProfileLanguage(RecordType):
    language: TD_Language

    languageCode: str

    name: TD_ProfileName


class TD_ProfileEmail(RecordType):
    id: str

    email: str


class TD_ProfileName(RecordType):
    firstName: str

    lastName: str