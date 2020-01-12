from space_sdk.space.projects.projects import Projects


def get_all_private_projects(projects: Projects):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_private-projects&endpoint=rest_query
    :param projects:
    :return:
    """
    urn: str = '/api/http/projects/private-projects'

    return projects.get(urn=urn)

