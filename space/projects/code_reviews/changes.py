from space.projects.projects import Projects

base_path: str = '/api/http/projects/key:{}/code-reviews/{}/changes'


def get_all_changes(projects: Projects, projectKey: str, reviewId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_changes&endpoint=rest_query
    :param projects:
    :param projectKey:
    :param reviewId:
    :return:
    """
    urn = base_path.format(projectKey, reviewId)
    return projects.get(urn=urn)
