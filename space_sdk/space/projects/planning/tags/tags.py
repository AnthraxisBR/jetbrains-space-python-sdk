from space_sdk.space_types.check_types import validate
from space_sdk.space.projects.projects import Projects
from space_sdk.space_types.tags import (
    HierarchicalTag
)


def create_hierarchical_tag(projects: Projects, hierarchical_tag: HierarchicalTag):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_tags&endpoint=rest_create
    :param issue:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/{}/planning/tags'
    urn: str = base_path.format(projects.project)

    data: dict = hierarchical_tag.__todict__('create')
    return projects.post(urn=urn, json=data)


def get_all_hierarchical_tags(projects: Projects, params=None):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_tags&endpoint=rest_query
    :param projects:
    :param params:
    :return:
    """

    if params is None:
        params = {}

    available_args: dict = {
        '$skip': str,  # skip
        '$top': int,  # $top
        'query': str  # query?
    }

    params = validate(params, available_args)

    base_path: str = '/api/http/projects/{}/planning/tags'
    urn: str = base_path.format(projects.project)

    return projects.get(urn=urn, params=params)
