from pendulum import (
    date, datetime
)
from ..base_type import RecordType
from ..avatar import AvatarCropSquare
from ..TD import *
from ..absence.absence import AbsenceRecord


class TD_MemberLocation(RecordType):
    id: str

    archived: bool

    location: TD_Location

    locationMapPoints: TD_LocationMapPoints

    member: TD_MemberProfile

    since: date

    till: date


class TD_MemberProfile(RecordType):
    id: str

    about: str

    absences: AbsenceRecord

    archived: bool

    avatar: str

    avatarCropSquare: AvatarCropSquare

    birthday: date

    emails: [TD_ProfileEmail]

    gender: str

    joined: date

    languages: [TD_ProfileLanguage]

    left: date

    leftAt: datetime

    links: [str]

    locations: [TD_MemberLocation]

    logins: str


class TD_Membership(RecordType):
    id: str

    activeSince: str

    activeTill: str

    approver: TD_MemberProfile

    archived: str

    editFor: str

    lead: bool

    manager: TD_MemberProfile
