from space_sdk.space_types.check_types import (
    is_str
)
from space_sdk.object_types.base_type import (
    RecordType
)

from ..TD.member import TD_MemberProfile

class SupportProfileDTO (RecordType):
    adminPermissionsGranted: bool

    profile: TD_MemberProfile