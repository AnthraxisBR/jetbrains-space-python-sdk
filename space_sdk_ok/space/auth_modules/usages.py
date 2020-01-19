from ..auth_modules.auth_modules import AuthModules


def get_all_usagesg(auth_modules: AuthModules):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=auth-modules_usages&endpoint=rest_query
    :param auth_modules:
    :param identifier:
    :return:
    """

    urn: str = auth_modules.mount_base_path('/usages')

    return auth_modules.delete(urn=urn)
