class TD_Team(RecordType):
    id: str

    archived: bool

    channelId: str

    description: str

    disbanded: bool

    disbandedAt: str

    email: str

    memberships: TD_Membership
