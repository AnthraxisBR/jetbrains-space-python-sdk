from pendulum import datetime
from .base_type import RecordType


class AccessRecord(RecordType):

    address: str

    time: datetime

    userAgent: str