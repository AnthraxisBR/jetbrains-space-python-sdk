from space_types.check_types import validate
from space_types.checklist import Checklist
from space.projects.projects import Projects


def create_checklist(projects: Projects, checklist: Checklist):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists&endpoint=rest_create
    :param projects:
    :param checklist:
    :return:
    """
    urn: str = '/api/http/projects/planning/checklists'

    data: dict = checklist.__todict__('create')
    return projects.post(urn=urn, json=data)


def get_all_checklists(projects: Projects, projectId=None):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists&endpoint=rest_query
    :param projects:
    :param projectId:
    :return:
    """
    if projectId is not None:
        params = {
            'projectId': projectId
        }
    else:
        params = {}

    available_args: dict = {
        'projectId': str
    }

    params = validate(params, available_args)

    urn: str = '/api/http/projects/planning/checklists'

    return projects.get(urn=urn, params=params)


def update_checklist(projects: Projects, checklistId: str, checklist: Checklist):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists&endpoint=rest_update_xxx
    :param projects:
    :param checklistId:
    :param checklist:
    :return:
    """
    base_path: str = '/api/http/projects/planning/checklists/{}'
    urn: str = base_path.format(str(checklistId))
    data: dict = checklist.__todict__('update')
    return projects.patch(urn=urn, json=data)


def delete_checklist(projects: Projects, checklistId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists&endpoint=rest_delete_xxx
    :param projects:
    :param checklistId:
    :return:
    """
    base_path: str = '/api/http/projects/planning/checklists/{}'
    urn: str = base_path.format(str(checklistId))

    return projects.delete(urn=urn)
