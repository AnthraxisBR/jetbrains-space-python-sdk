from space_sdk.space.projects.projects import Projects


def edit_review_participant(projects: Projects, reviewId: str, user: str,
                            role: str = False,
                            state: str = False
                            ):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_participants&endpoint=rest_update_xxx
    :param role:
    :param state:
    :param projects:
    :param projectKey:
    :param reviewId:
    :param user:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/participants/{}')
    urn = base_path.format(projects.project, reviewId, user)

    data = {}

    if role or role is None:
        data['role'] = role

    if state or state is None:
        data['state'] = state

    return projects.patch(urn=urn, data=data)
