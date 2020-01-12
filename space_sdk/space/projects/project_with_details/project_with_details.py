from space_sdk.space.projects.projects import Projects


def get_all_projects_with_details_by_member(projects: Projects, member: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_projects-with-details&endpoint=rest_query_member%3Axxx
    :param projects:
    :param member:
    :return:
    """
    base_path: str = '/api/http/projects/projects-with-details/member:{}'
    urn: str = base_path.format(member)

    return projects.get(urn=urn)

