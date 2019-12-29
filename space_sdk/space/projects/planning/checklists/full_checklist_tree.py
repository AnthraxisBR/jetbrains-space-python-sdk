from space_sdk.space.projects.projects import Projects


def get_full_checklist_tree(projects: Projects, checklistId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists_xxx_full-checklist-tree&endpoint=rest_get
    :param projects:
    :param checklistId:
    :return:
    """
    base_path: str = '/api/http/projects/planning/checklists/{}/full-checklist-tree'
    urn = base_path.format(checklistId)
    return projects.get(urn=urn)