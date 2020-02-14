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


class BG_ArticleId(RecordType):
    id: str

class BG_ArticleAlias(RecordType):
    alias: str

    created: datetime