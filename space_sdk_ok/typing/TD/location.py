from ..base_type import RecordType


class TD_Location(RecordType):
    id: str

    address: str

    archived: bool

    channelId: str

    description: str

    email: str

    equipment: str

    mapId: str

    name: str

    parent: str

    phone: str

    type: str

    tz: str

    workdays: int


class TD_LocationMapPoints(RecordType):
    id: str

    created: str

    deleted: bool

    mapId: str

    memberLocation: str

    x: int

    y: int
