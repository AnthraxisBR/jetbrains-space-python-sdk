from space_sdk_ok.typing.base_type import (
    RecordType
)

from space_sdk_ok.typing.access import (
    AccessRecord
)

class ES_AuthModuleSettings(RecordType):
    pass


class ES_AuthModule(RecordType):

    id: str

    enabled: bool

    iconDataUri: str

    key: str

    name: str

    ordinal: int




class ES_ProfileLogin(RecordType):

    access: AccessRecord

    authModule: ES_AuthModule

    details: str
