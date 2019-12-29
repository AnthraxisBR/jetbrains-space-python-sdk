from space_sdk.space_types.check_types import validate
from space_sdk.space.projects.projects import Projects


def get_all_code_reviews(projects: Projects, params=None):

    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews&endpoint=rest_query
    :param projects:
    :param params:
    :return:
    """

    if params is None:
        params = {}
    available_args: dict = {
        '$skip': str,
        '$top': int,
        'state': str,  # CodeReviewState?
        'text': str,  # string?
        'authorProfileId': str,  # string?
        'authorGitName': str,
        'authorGitEmail': str,  # string?
        'to': str,  # date?
        'sort': str,  # CreatedAtDesc
        'reviewer': str,  # string?
        'type': str  # ReviewType?
    }

    params = validate(params, available_args)

    base_path: str = projects.mount_base_path('code-reviews')
    urn = base_path.format(projects.project)
    return projects.get(urn=urn, params=params)


def get_code_review_by_review_number(projects: Projects, reviewNumber: int):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews&endpoint=rest_get_review-number%3Axxx
    :param projects:
    :param reviewNumber:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/review-number:{}')
    urn = base_path.format(projects.project, str(reviewNumber))
    return projects.get(urn=urn)


def get_review_counts(projects: Projects):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews&endpoint=http_get_review-counts
    :param projects:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/review-counts')
    urn = base_path.format(projects.project)
    return projects.get(urn=urn)


def mark_review_as_read(projects: Projects, reviewNumber: int):
    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews&endpoint=http_post_xxx_mark-as-read
    :param projects:
    :param reviewNumber:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/{}/mark-as-read')
    urn = base_path.format(projects.project, str(reviewNumber))
    return projects.post(urn=urn)
