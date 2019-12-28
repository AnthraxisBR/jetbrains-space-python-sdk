from helper.check_types import validate
from helper.check_types import validate
from space.projects.projects import Projects


def add_member(projects: Projects, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_members&endpoint=rest_create
    :param projects:
    :param profileId:
    :return:
    """
    base_path: str = projects.mount_base_path('members')
    urn = base_path.format(projects.project)
    data: dict = {
        'profileId': profileId
    }
    return projects.post(urn=urn, data=data)


def get_all_members(projects: Projects, profileId: str, params=None):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_members&endpoint=rest_query
    :param projects:
    :param profileId:
    :param params:
    :return:
    """
    if params is None:
        params = {}

    available_args: dict = {
        '$skip': str,
        '$top': int,
        'query': str,  # CodeReviewState?
    }

    params = validate(params=params, comparable=available_args)
    base_path: str = projects.mount_base_path('members')
    urn = base_path.format(projects.project)
    return projects.post(urn=urn, params=params)


def remove_member(projects: Projects, profileId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_xxx_members&endpoint=rest_delete_xxx
    :param projects:
    :param profileId:
    :return:
    """
    base_path: str = projects.mount_base_path('members/{}')
    urn = base_path.format(projects.project, profileId)
    return projects.delete(urn=urn)