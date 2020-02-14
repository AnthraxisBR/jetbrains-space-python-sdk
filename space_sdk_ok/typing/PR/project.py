from pendulum import datetime
from ..base_type import (
    RecordType,
    RequestType
)

from ...typing.check_types import (
    required,
    is_str,
    is_bool,
    is_instance_of,
    is_date
)

from ..TD.member import (
    TD_MemberProfile,
)
from ..TD.team import (
    TD_Team,
)

class ProjectKey(RecordType):
    key: str


class LastActivity(dict):
    first: datetime

    second: int

class RepositoryActivity(RecordType):
    lastActivity: LastActivity

class PR_RepositoryInfo(RecordType):
    description: str

    initProgress: str

    latestActivity: datetime

    name: str

    proxyPushNotification: datetime

    readmeName: str

    state: str

class PR_Project(RecordType):
    id: str

    adminProfiles: [TD_MemberProfile]

    adminTeams: [TD_Team]

    archived: bool

    description: str

    icon: str

    key: ProjectKey

    latestRepositoryActivity: datetime

    memberProfiles: [TD_MemberProfile]

    memberTeams: [TD_Team]

    name: str

    private: bool

    repos: [PR_RepositoryInfo]

    tags: [str]