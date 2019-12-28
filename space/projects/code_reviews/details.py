from space.projects.projects import Projects


def get_details_details(projects: Projects, reviewId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_details&endpoint=rest_get
    :param projects:
    :param reviewId:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/details')
    urn = base_path.format(projects.project, reviewId)
    return projects.get(urn=urn)
