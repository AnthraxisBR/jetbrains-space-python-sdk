from space_sdk.space.projects.projects import Projects


def get_all_full_projects_by_member(projects: Projects, member: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_full-projects&endpoint=rest_query_member%3Axxx
    :param projects:
    :param member:
    :return:
    """
    base_path: str = '/api/http/projects/full-projects'
    base_path += 'member:{}'
    urn = base_path.format(member)
    return projects.get(urn=urn)


def get_all_full_projects_by_team(projects: Projects, teamId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_full-projects&endpoint=rest_query_team%3Axxx
    :param projects:
    :param teamId:
    :return:
    """
    base_path: str = '/api/http/projects/full-projects'
    base_path += 'team:{}'
    urn = base_path.format(teamId)
    return projects.get(urn=urn)


def get_full_project(projects: Projects, id: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_full-projects&endpoint=rest_get_xxx
    :param projects:
    :param id:
    :return:
    """
    base_path: str = '/api/http/projects/full-projects'
    base_path += '{}'
    urn = base_path.format(id)
    return projects.get(urn=urn)


def get_full_project_by_key(projects: Projects, projectId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_full-projects&endpoint=rest_get_key%3Axxx
    :param projects:
    :param projectId:
    :return:
    """
    base_path: str = '/api/http/projects/full-projects'
    base_path += 'key:{}'
    urn = base_path.format(projectId)
    return projects.get(urn=urn)
