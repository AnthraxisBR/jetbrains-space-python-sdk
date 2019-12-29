from space_sdk.space.projects.projects import Projects


def get_all_starred_checklist(projects: Projects):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_checklists_starred&endpoint=rest_query
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/planning/checklists/{}/full-checklist-tree'
    return projects.get(urn=base_path)