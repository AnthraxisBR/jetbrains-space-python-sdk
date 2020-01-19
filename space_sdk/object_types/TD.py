from space_sdk import *
from .base_type import *
from pendulum import date


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

    approver: TD_MemberProfile

    archived: str

    editFor: str

    lead: bool

    manager: TD_MemberProfile







class TD_Team(RecordType):

    id: str

    archived: bool

    channelId: str

    description: str

    disbanded: bool

    disbandedAt: str

    email: str

    memberships: TD_Membership




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

