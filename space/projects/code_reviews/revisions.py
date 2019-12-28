from space.projects.projects import Projects
from space_types.revisions import (
    Revisions
)


def add_revisions_to_review(projects: Projects, reviewId: str, revisions: Revisions):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_revisions&endpoint=rest_create
    :param projects:
    :param projectKey:
    :param reviewId:
    :param revisions:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/revisions')
    urn: str = base_path.format(projects.project, reviewId)

    data: dict = revisions.__todict__()

    return projects.post(urn=urn, data=data)


def remove_revisions_from_review(projects: Projects, reviewId: str, revisions: list):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_revisions&endpoint=rest_delete
    :param projects:
    :param projectKey:
    :param reviewId:
    :param revisions:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/revisions')
    urn: str = base_path.format(projects.project, reviewId)

    data: dict = {
        'revisions': revisions
    }

    return projects.delete(urn=urn, params=data)
