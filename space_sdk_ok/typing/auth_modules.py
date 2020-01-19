from pendulum import date
from .base_type import RecordType


class SSLKeyStore(RecordType):
    created: date

    name: str


class ES_TeamMapping(RecordType):
    externalGroupName: str

    teamId: str


class ES_GithubAuthModuleSettings(RecordType):
    clientId: str

    clientSecret: str

    githubUrl: str

    organizations: str

    registerNewUsers: str


class ES_GoogleAuthModuleSettings(RecordType):
    clientId: str

    clientSecret: str

    domains: str

    registerNewUsers: str


class ES_HubAuthModuleSettings(RecordType):
    clientId: str

    clientSecret: str

    groups: [str]

    hubUrl: str

    orgAuthProviderName: str

    registerNewUsers: bool


class ES_BuiltinAuthModuleSettings(RecordType):
    domains: str

    passwordStrengthPolicy: bool


class ES_LdapAttributeNames(RecordType):
    emailAttributeName: str

    fullNameAttributeName: str

    groupsAttributeName: str

    usernameAttributeName: str


class ES_ProfileLoginDetails(RecordType):
    pass


class ES_BuiltinProfileLoginDetails(ES_ProfileLoginDetails):
    passwordChangeRequest: str

    passwordName: str


class ES_GithubProfileLoginDetails(ES_ProfileLoginDetails):
    avatarUrl: str

    email: str

    emailVerified: str

    firstName: str

    lastName: str

    login: str

    organizations: [str]


class ES_HubProfileLoginDetails(ES_ProfileLoginDetails):
    avatarUrl: str

    email: str

    emailVerified: bool

    firstName: str

    hubAuthModuleLogin: str

    lastName: str

    login: str


class ES_DefaultProfileLoginDetails(ES_ProfileLoginDetails):
    avatarUrl: str

    email: str

    emailVerified: str

    firstName: str

    lastName: str

    login: str


class ES_LdapAuthModuleSettings(RecordType):
    attributeNames: ES_LdapAttributeNames

    bindUserDN: str

    bindUserPassword: str

    connectionTimeout: int

    filter: str

    readTimeout: int

    referralIgnored: bool

    registerNewUsers: bool

    serverUrl: str

    sslKeyStore: SSLKeyStore

    teamMappings: ES_TeamMapping

    type: str
