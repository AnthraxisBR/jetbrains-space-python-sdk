from space_sdk.space.projects.projects import Projects
from space_sdk.space_types.issue import (
    Issue, IssueResolved
)


def create_issue(projects: Projects, issue: Issue):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_issues&endpoint=rest_create
    :param issue:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/{}/planning/issues'
    urn: str = base_path.format(projects.project)

    data: dict = issue.__todict__('create')
    return projects.post(urn=urn, json=data)


def get_all_issues(projects: Projects):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_issues&endpoint=rest_query
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/{}/planning/issues'
    urn: str = base_path.format(projects.project)

    return projects.get(urn=urn)


def get_issue_by_number(projects: Projects, number: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_issues&endpoint=rest_query
    :param number:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/{}/planning/issues/number:{}'
    urn: str = base_path.format(projects.project, number)

    return projects.get(urn=urn)


def update_issue(projects: Projects, issue: Issue):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_issues&endpoint=rest_update_xxx
    :param issue:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/{}/planning/issues'
    urn: str = base_path.format(projects.project)

    data: dict = issue.__todict__('update')
    return projects.patch(urn=urn, json=data)


def delete_issue(projects: Projects, issueId: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_issues&endpoint=rest_delete_xxx
    :param number:
    :param projects:
    :return:
    """
    base_path: str = '/api/http/projects/planning/issues/{}'
    urn: str = base_path.format(issueId)

    return projects.delete(urn=urn)


def toggle_issue_resolved(projects: Projects, issueId: str, issue_resolved: IssueResolved):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_planning_issues&endpoint=http_post_xxx_toggle-resolved
    :param projects:
    :param issueId:
    :param issue_resolved
    :return:
    """
    base_path: str = '/api/http/projects/planning/issues/{}/toggle-resolved'
    urn: str = base_path.format(issueId)

    data: dict = issue_resolved.__todict__()
    return projects.post(urn=urn, json=data)
