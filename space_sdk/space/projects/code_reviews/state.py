from space_sdk.space_types.state import State
from space_sdk.space.projects.projects import Projects


def edit_review_state(projects: Projects, reviewId: str, state: State):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_xxx_state&endpoint=rest_update
    :param projects:
    :param reviewId:
    :param state:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/state')
    urn: str = base_path.format(projects.project, reviewId)

    data: dict = {
        'state': state
    }

    return projects.patch(urn=urn, data=data)
