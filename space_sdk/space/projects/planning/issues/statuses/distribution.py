from space_sdk.space.projects.projects import Projects


def get_issue_status_distribution(projects: Projects):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_xxx_planning_issues_statuses_distribution&endpoint=rest_get
    :param projects:
    :return:
    """
    base_path: str = projects.mount_base_path('/planning/issues/statuses/distribution')
    urn = base_path.format(projects.project)

    return projects.get(urn=urn)
