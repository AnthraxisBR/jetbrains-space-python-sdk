from space_sdk import *
from space_sdk.space_types.check_types import (
    is_str, required, is_bool
)
from space_sdk.object_types.base_type import (
    RequestType, RecordType
)
from space_sdk.object_types.absence.absence_reason import (
    AbsenceReasonRecord
)


class AbsencesSubscriptions(RequestType):
    locationId = [is_str]

    teamId = [is_str]

    reasonId = [is_str]


class TD_Location(RecordType):
    id: str

    address: str

    archived: bool

    channelId: str

    description: str

    email: str

    equipment: str

    mapId: str

    name: str

    parent: str

    phone: str

    type: str

    tz: str

    workdays: int


class AvatarCropSquare(RecordType):

    length: int

    x: int

    y: int

class TD_ProfileEmail(RecordType):

    id: str

    email: str


class TD_ProfileName(RecordType):

    firstName: str

    lastName: str

class TD_Language(RecordType):
    id: str

    code: str

    firstNameTitle: str

    lastNameTitle: str

    name: str

    nativeName: str


class TD_ProfileLanguage(RecordType):
    language: TD_Language

    languageCode: str

    name: TD_ProfileName

class TD_LocationMapPoints(RecordType):

    id: str

    created: str

    deleted: bool

    mapId: str

    memberLocation: str

    x: int

    y: int





class TD_MemberProfile(RecordType):

    id: str

    about: str

    absences: AbsenceRecord

    archived: bool

    avatar: str

    avatarCropSquare: AvatarCropSquare

    birthday: str

    emails: [TD_ProfileEmail]

    gender: str

    joined: str

    languages: [TD_ProfileLanguage]

    left: str

    leftAt: str

    links: [str]

    locations: [TD_MemberLocation]

    logins:





class TD_MemberLocation(RecordType):
    id: str

    archived: str

    location: TD_Location

    locationMapPoints: [TD_LocationMapPoints]

    member: TD_MemberProfile


class TD_Membership(RecordType):

    id: str

    activeSince: str

    activeTill: str

    approver: str

    archived: str

    editFor: str

    lead: bool

    manager:





class TD_Team(RecordType):

    id: str

    archived: bool

    channelId: str

    description: str

    disbanded: bool

    disbandedAt: str

    email: str

    memberships:



class AbsencesSubscriptionRecord(RecordType):
    id: str

    approvalRequired: bool

    archived: bool

    defaultAvailability: bool

    description: str

    icon: str

    name: str

    reason: AbsenceReasonRecord
