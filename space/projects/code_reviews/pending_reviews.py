from space.projects.projects import Projects


def get_pending_reviews_count(projects: Projects):

    """
        https://ltinteg.jetbrains.space/httpApiPlayground?resource=projects_key%3Axxx_code-reviews_pending-reviews&endpoint=http_get_count
    :param projects:
    :param projectKey:
    :return:
    """
    base_path: str = projects.mount_base_path('code-reviews/pending-reviews/count')
    urn = base_path.format(projects.project)
    return projects.get(urn=urn)
