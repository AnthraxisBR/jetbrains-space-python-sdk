from space.projects.projects import Projects

base_path: str = '/api/http/projects/key:{}/code-reviews/{}/revisions'


def add_revisions_to_review(projects: Projects, projectKey: str, reviewId: str, state: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_state&endpoint=rest_update
    :param projects:
    :param projectKey:
    :param reviewId:
    :param state:
    :return:
    """
    urn: str = base_path.format(projectKey, reviewId)

    data: dict = {
        'state': state
    }

    return projects.patch(urn=urn, data=data)