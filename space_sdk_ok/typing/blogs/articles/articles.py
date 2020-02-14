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

from ...BG.article import (
    BG_ArticleAlias,
    BG_ArticleId
)

from ...PR.project import (
    PR_Project,
)

from ...TD.location import (
    TD_Location,
)

class ArticleAliasRequest(RequestType):
    title = [required, is_str]

    content = [required, is_str]

    created = [is_date]

    team = [is_str]

    location = [is_str]

class M2ChannelContentRecord(RecordType):
    id: str

    content: str #TODO M2ChannelContactInfo

class ParticipantRecord(RecordType):
    status: str

    user: TD_MemberProfile

class ATimeZone(RecordType):
    id: str

class MeetingRecord(RecordType):
    id: str

    allDay: bool

    archived: bool

    article: ArticleRecord

    finishes: datetime

    participants: [ParticipantRecord]

    rooms: [TD_Location]

    starts: datetime

    timezone: ATimeZone

class ArticleMarkdownImage(RecordType):
    alt: str

    src: str

class EmojiReactionRecord(RecordType):
    id: str

    count: int

    emoji: str

    itemId: str

    meReacted: bool

    order: str


class CertainReactionToItemRecord(RecordType):
    id: str

    count: int

    emoji: str

    itemId: str

    meReacted: bool

    order: str


class AllReactionsToItemRecord(RecordType):
    id: str

    emojiReactions: EmojiReactionRecord

    reactions: CertainReactionToItemRecord

class ArticleRecord(RecordType):

    id: str

    aliases: BG_ArticleAlias

    archived: bool

    author: TD_MemberProfile

    channel: M2ChannelContentRecord

    created: datetime

    editable: bool

    event: MeetingRecord

    location: TD_Location

    preview: str

    previewImages = [ArticleMarkdownImage]

    project: PR_Project

    reactions: AllReactionsToItemRecord

    team: TD_Team

    title: str