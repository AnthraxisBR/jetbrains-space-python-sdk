from pendulum import datetime
from ..base_type import (
    RecordType,
    RequestType
)

from .member import TD_Membership

class TD_Team(RecordType):
    id: str

    archived: bool

    channelId: str

    description: str

    disbanded: bool

    disbandedAt: str

    email: str

    memberships: TD_Membership
