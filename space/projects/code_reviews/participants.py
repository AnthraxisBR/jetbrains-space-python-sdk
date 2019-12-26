from space.projects.projects import Projects

base_path: str = '/api/http/projects/key:{}/code-reviews/{}/participants/{}'


def edit_review_participant(projects: Projects, projectKey: str, reviewId: str, user: str,
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
    urn = base_path.format(projectKey, reviewId, user)
    data = {}

    if role or role is None:
        data['role'] = role

    if state or state is None:
        data['state'] = state

    return projects.patch(urn=urn, data=data)
