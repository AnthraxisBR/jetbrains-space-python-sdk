from space.projects.projects import Projects

base_path: str = '/api/http/projects/key:{}/code-reviews/pending-reviews/count'


def get_details_details(projects: Projects, projectKey: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_pending-reviews&endpoint=http_get_count
    :param projects:
    :param projectKey:
    :return:
    """
    urn = base_path.format(projectKey)
    return projects.get(urn=urn)
