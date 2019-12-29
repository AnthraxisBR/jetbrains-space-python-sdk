from space_sdk.space.projects.projects import Projects

base_path: str = '/api/http/projects/{}/administrators'


def add_administrator(projects: Projects, projectId: str, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_administrators_members&endpoint=rest_create
    :param projects:
    :param projectId:
    :param profileId:
    :return:
    """
    urn = base_path.format(projectId) + '/members'
    return projects.post(urn=urn, data={
        'profileId': profileId
    })


def remove_administrator(projects: Projects, projectId: str, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_administrators_members&endpoint=rest_delete_xxx
    :param projects:
    :param projectId:
    :param profileId:
    :return:
    """
    urn = base_path.format(projectId) + '/members/{}'.format(profileId)
    return projects.delete(urn)
