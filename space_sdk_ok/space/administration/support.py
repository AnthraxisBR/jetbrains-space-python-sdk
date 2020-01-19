from ..administration.administration import Administration


def create_absences_reason(administration: Administration):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=administration_support&endpoint=rest_create
    :param administration:g
    :return:
    """
    urn: str = administration.mount_base_path('/support')

    return administration.post(urn=urn)
