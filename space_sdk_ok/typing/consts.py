

null: str = 'null'
All: str = 'All'
WithAccessibleReasonUnapproved: str = 'WithAccessibleReasonUnapproved'
WithAccessibleReasonAll: str = 'WithAccessibleReasonAll'
Opened: str = 'Opened'
Closed: str = 'Closed'
Deleted: str = 'Deleted'
CreatedAtAsc: str = 'CreatedAtAsc'
CreatedAtDesc: str = 'CreatedAtDesc'
LastUpdatedAtAsc: str = 'LastUpdatedAtAsc'
LastUpdatedDesc: str = 'LastUpdatedDesc'
CommitSetReview: str = 'CommitSetReview'
MergeRequest: str = 'MergeRequest'
ADDED: str = 'ADDED'
DELETED: str = 'DELETED'
MODIFIED: str = 'MODIFIED'
FILE: str = 'FILE'
DIR: str = 'DIR'
GIT_LINK: str = 'GIT_LINK'
SYM_LINK: str = 'SYM_LINK'

BooleanCFValue: str = 'BooleanCFValue'
DateCFValue: str = 'DateCFValue'
EnumCFValue: str = 'EnumCFValue'
EnumListCFValue: str = 'EnumListCFValue'
IntCFValue: str = 'IntCFValue'
IntListCFValue: str = 'IntListCFValue'
ProfileCFValue: str = 'ProfileCFValue'
ProfileListCFValue: str = 'ProfileListCFValue'
StringCFValue: str = 'StringCFValue'
StringListCFValue: str = 'StringListCFValue'
UrlCFValue: str = 'UrlCFValue'


changeTypes: list = [
    ADDED, DELETED, MODIFIED
]

CF_values: list = [
    BooleanCFValue,
    DateCFValue,
    EnumCFValue,
    EnumListCFValue,
    IntCFValue,
    IntListCFValue,
    ProfileCFValue,
    ProfileListCFValue,
    StringCFValue,
    StringListCFValue,
    UrlCFValue
]

viewMode: list = [
    All,
    WithAccessibleReasonAll,
    WithAccessibleReasonUnapproved
]
