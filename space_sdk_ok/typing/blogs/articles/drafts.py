from pendulum import datetime
from ...base_type import (
    RecordType,
    RequestType
)

from ....typing.check_types import (
    required,
    is_str,
    is_bool,
    is_instance_of,
    is_date
)

from ...TD.member import (
    TD_MemberProfile,
)

from ...TD.team import (
    TD_Team,
)

from ...TD.location import (
    TD_Location,
)


from ...PR.project import (
    PR_Project,
)

class DR_DraftId(RecordType):
    id: str
