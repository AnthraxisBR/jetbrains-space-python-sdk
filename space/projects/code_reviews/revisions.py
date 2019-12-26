from space.projects.projects import Projects
from lib.types import (
    AddRevisions, RemoveRevisions
)

base_path: str = '/api/http/projects/key:{}/code-reviews/{}/revisions'


def add_revisions_to_review(projects: Projects, projectKey: str, reviewId: str, revisions: AddRevisions):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_revisions&endpoint=rest_create
    :param projects:
    :param projectKey:
    :param reviewId:
    :param revisions:
    :return:
    """
    urn: str = base_path.format(projectKey, reviewId)

    data: dict = revisions.asdict()

    return projects.post(urn=urn, data=data)


def remove_revisions_from_review(projects: Projects, projectKey: str, reviewId: str, revisions: RemoveRevisions):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_revisions&endpoint=rest_delete
    :param projects:
    :param projectKey:
    :param reviewId:
    :param revisions:
    :return:
    """
    urn: str = base_path.format(projectKey, reviewId)

    data: dict = revisions.asdict()

    return projects.delete(urn=urn, params=data)
