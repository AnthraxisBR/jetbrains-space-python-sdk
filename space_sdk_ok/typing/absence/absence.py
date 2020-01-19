from pendulum import datetime
from ..base_type import RecordType
from ..TD.member import TD_MemberProfile


class AbsenceApprovalRecord(RecordType):
    approved: str

    approvedAt: datetime

    approvedBy: TD_MemberProfile


class AbsenceRecord(RecordType):
    id: str
