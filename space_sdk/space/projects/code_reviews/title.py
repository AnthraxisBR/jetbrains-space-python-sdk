from space_sdk.space.projects.projects import Projects


def edit_review_title(projects: Projects, reviewId: str, title: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_title&endpoint=rest_update
    :param projects:
    :param reviewId:
    :param title:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/title')
    urn: str = base_path.format(projects.project, reviewId)

    data: dict = {
        'title': title
    }

    return projects.patch(urn=urn, data=data)