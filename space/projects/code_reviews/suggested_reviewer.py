from space_types.state import State
from space.projects.projects import Projects


def get_all_suggested_reviewer(projects: Projects, reviewId: str):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_suggested-reviewers&endpoint=rest_query
    :param projects:
    :param reviewId:
    :param state:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/suggested-reviewers')
    urn: str = base_path.format(projects.project, reviewId)

    return projects.get(urn=urn)
