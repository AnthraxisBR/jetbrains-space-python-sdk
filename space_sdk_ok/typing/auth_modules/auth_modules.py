from pendulum import datetime
from ..base_type import (
    RecordType,
    RequestType
)
from ..ES import ES_AuthModuleSettings

from ...typing.check_types import (
    required,
    is_str,
    is_bool,
    is_instance_of
)


class AuthModuleRequest(RequestType):
    key = [required, is_str]

    name = [required, is_str]

    enabled = [is_bool]

    settings = [is_instance_of, ES_AuthModuleSettings]
