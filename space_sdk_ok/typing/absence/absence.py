from pendulum import datetime
from ..base_type import (
    RecordType,
    RequestType
)
from ..TD.member import TD_MemberProfile

from ...typing.check_types import (
    required,
    is_str,
    is_bool,
    is_date
)


class Absence(RequestType):
    member = [required, is_str]

    reason = [required, is_str]

    description = [required, is_str]

    location = [is_str]

    since = [required, is_date]

    till = [required, is_date]

    available = [required, is_bool]

    icon = [required, is_str]

    # TODO: Custom Field Value


class AbsenceApprovalRecord(RecordType):
    approved: str

    approvedAt: datetime

    approvedBy: TD_MemberProfile


class AbsenceRecord(RecordType):
    id: str

    approval: AbsenceApprovalRecord

    archived: bool

    available: bool

