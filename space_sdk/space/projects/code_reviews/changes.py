from space_sdk.space.projects.projects import Projects


def get_all_changes(projects: Projects, reviewId: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_changes&endpoint=rest_query
    :param projects:
    :param reviewId:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/changes')
    urn = base_path.format(projects.project, reviewId)
    return projects.get(urn=urn)
