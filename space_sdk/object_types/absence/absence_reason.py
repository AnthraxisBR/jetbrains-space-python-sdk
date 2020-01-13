from space_sdk import *
from space_sdk.space_types.check_types import (
    is_str, required, is_bool
)
from space_sdk.object_types.base_type import (
    RequestType, RecordType
)


class AbsencesAbsenceReason(RequestType):
    name = [required, is_str]

    description = [required, is_str]

    defaultAvailability = [required, is_bool]

    approvalRequired = [required, is_bool]

    icon = [is_str]


class AbsenceReasonRecord(RecordType):
    id: str

    approvalRequired: bool

    archived: bool

    defaultAvailability: bool

    description: str

    icon: str

    name: str
