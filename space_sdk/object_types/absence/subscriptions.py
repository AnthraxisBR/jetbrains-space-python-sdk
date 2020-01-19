from space_sdk import *
from space_sdk.space_types.check_types import (
    is_str, required, is_bool
)
from space_sdk.object_types.base_type import (
    RequestType, RecordType
)
from space_sdk.object_types.absence.absence_reason import (
    AbsenceReasonRecord
)




class AbsencesSubscriptions(RequestType):
    locationId = [is_str]

    teamId = [is_str]

    reasonId = [is_str]


class AbsencesSubscriptionRecord(RecordType):
    id: str

    approvalRequired: bool

    archived: bool

    defaultAvailability: bool

    description: str

    icon: str

    name: str

    reason: AbsenceReasonRecord
