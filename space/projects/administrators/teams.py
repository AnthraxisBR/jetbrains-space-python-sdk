from space.projects.projects import Projects

base_path: str = '/api/http/projects/{}/administrators'


def add_administrator_team(projects: Projects, projectId: str, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_administrators_teams&endpoint=rest_create
    :param projects:
    :param projectId:
    :param profileId:
    :return:
    """
    urn = base_path.format(projectId) + '/teams'
    return projects.post(urn=urn, data={
        'profileId': profileId
    })


def remove_administrator_team(projects: Projects, projectId: str, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_administrators_teams&endpoint=rest_delete_xxx
    :param projects:
    :param projectId:
    :param profileId:
    :return:
    """
    urn = base_path.format(projectId) + '/teams/{}'.format(profileId)
    return projects.delete(urn)
