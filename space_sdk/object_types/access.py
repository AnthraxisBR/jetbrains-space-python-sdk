from pendulum import datetime

from space_sdk.object_types.base_type import (
    RecordType
)


class AccessRecord(RecordType):

    address: str

    time: datetime

    userAgent: str