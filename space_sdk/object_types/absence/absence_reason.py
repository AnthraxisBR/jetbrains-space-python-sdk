from ..rule import Rule

from ..base_type import (
    RequestType,
    RecordType
)

from ...space_types.check_types import (
    required,
    is_str,
    is_bool
)


class AbsencesAbsenceReasonRequest(RequestType):
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
