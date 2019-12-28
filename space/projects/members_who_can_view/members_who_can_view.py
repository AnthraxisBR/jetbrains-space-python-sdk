from helper.check_types import validate
from helper.check_types import validate
from space.projects.projects import Projects


def get_all_members_who_can_view(projects: Projects, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_members-who-can-view&endpoint=rest_query
    :param projects:
    :param profileId:
    :return:
    """
    base_path: str = projects.mount_base_path('members-who-can-view')
    urn = base_path.format(projects.project)
    data: dict = {
        'profileId': profileId
    }
    return projects.post(urn=urn, data=data)
