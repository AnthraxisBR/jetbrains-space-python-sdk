from space.projects.projects import Projects

base_path: str = '/api/http/projects/key:{}/code-reviews/{}/details'


def get_details_details(projects: Projects, projectKey: str, reviewId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_details&endpoint=rest_get
    :param projects:
    :param projectKey:
    :param reviewId:
    :return:
    """
    urn = base_path.format(projectKey, reviewId)
    return projects.get(urn=urn)
