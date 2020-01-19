from ...typing.absence.subscriptions import AbsencesSubscriptionsRequest
from ..absence.absence import Absence


def create_absences_subscription(absence: Absence, absences_subscriptions: AbsencesSubscriptionsRequest):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_subscriptions&endpoint=rest_create
    :param absence:
    :param absences_subscriptions:
    :return:
    """
    urn: str = absence.mount_base_path('/subscriptions')

    absences_subscriptions.validate_object(absences_subscriptions.kwargs)

    return absence.post(urn=urn, data=absences_subscriptions.__dict__())


def get_all_absences_subscriptions(absence: Absence):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_subscriptions&endpoint=rest_query
    :param absence:
    :return:
    """
    urn: str = absence.mount_base_path('/subscriptions')

    return absence.get(urn=urn)


def update_absences_subscription(absence: Absence, absence_subscription_id: str, absences_subscriptions: AbsencesSubscriptionsRequest):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_subscriptions&endpoint=rest_update_xxx
    :param absence:
    :param absence_subscription_id:
    :param absences_subscriptions:
    :return:
    """
    base_path: str = absence.mount_base_path('/subscriptions/{}')
    urn = base_path.format(absence_subscription_id)

    absences_subscriptions.validate_object(absences_subscriptions.kwargs)

    return absence.patch(urn=urn, data=absences_subscriptions.__dict__())


def delete_absences_subscriptions(absence: Absence, absence_subscription_id: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_subscriptions&endpoint=rest_query
    :param absence:
    :param absence_subscription_id:
    :return:
    """
    base_path: str = absence.mount_base_path('/subscriptions/{}')
    urn = base_path.format(absence_subscription_id)

    return absence.delete(urn=urn)