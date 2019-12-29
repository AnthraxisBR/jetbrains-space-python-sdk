from space_sdk.space.projects.projects import Projects


def get_all_unread_revisions(projects: Projects, reviewId: str, title: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_unread-revisions&endpoint=rest_query
    :param projects:
    :param reviewId:
    :param title:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/unread-revisions')
    urn: str = base_path.format(projects.project, reviewId)

    return projects.get(urn=urn)