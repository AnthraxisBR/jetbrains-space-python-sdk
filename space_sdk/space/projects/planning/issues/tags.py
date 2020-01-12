from space_sdk.space.projects.projects import Projects


def add_issue_tag(projects: Projects, issueId: str, tagId: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_issues_xxx_tags&endpoint=rest_create_xxx
    :param issueId:
    :param tagId:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/planning/issues'
    base_path += '/{}/tags/{}'
    urn = base_path.format(issueId, tagId)
    return projects.post(urn=urn)


def remove_issue_tag(projects: Projects, issueId: str, tagId: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_issues_xxx_tags&endpoint=rest_delete_xxx
    :param issueId:
    :param tagId:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/planning/issues'
    base_path += '/{}/tags/{}'
    urn = base_path.format(issueId, tagId)
    return projects.delete(urn=urn)
