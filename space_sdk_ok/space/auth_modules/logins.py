from ..auth_modules.auth_modules import AuthModules


def delete_login(auth_modules: AuthModules, auth_module_id: str, identifier: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=auth-modules_xxx_logins&endpoint=rest_delete_xxx
    :param auth_modules:
    :param auth_module_id:
    :param identifier:
    :return:
    """

    base_path: str = auth_modules.mount_base_path('/{}/logins/{}')
    urn = base_path.format(auth_module_id, identifier)

    return auth_modules.delete(urn=urn)
