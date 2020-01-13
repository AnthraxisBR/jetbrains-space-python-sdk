from space_sdk.space_types.check_types import validate
from space_sdk.space.projects.projects import Projects


def get_all_code_reviews(projects: Projects, repository: str, params=None):

    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews&endpoint=rest_query
    :param projects:
    :param repository
    :param params:
    :return:
    """

    if params is None:
        params = {}
    available_args: dict = {
        'revisions': str,
    }

    params = validate(params, available_args)

    base_path: str = projects.mount_base_path('/repositories/{}/code-discussions')
    urn = base_path.format(projects.project, repository)
    return projects.get(urn=urn, params=params)

