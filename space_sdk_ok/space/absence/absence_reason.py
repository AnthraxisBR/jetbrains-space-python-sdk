from ...typing.check_types import validate
from ...typing.absence.absence_reason import AbsencesAbsenceReasonRequest
from ..absence.absence import Absence


def create_absences_reason(absence: Absence, absence_reason: AbsencesAbsenceReasonRequest):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_absence-reasons&endpoint=rest_create
    :param absence:
    :param absence_reason:
    :return:
    """
    urn: str = absence.mount_base_path('/absence-reasons')

    absence_reason.validate_object(absence_reason.kwargs)

    return absence.post(urn=urn, data=absence_reason.__dict__())


def create_absences_reason_in_absence_reason(absence: Absence, absence_reason_id: str,
                                            absence_reason: AbsencesAbsenceReasonRequest):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_absence-reasons&endpoint=rest_create_xxx
    :param absence:
    :param absence_reason_id:
    :param absence_reason:
    :return:
    """
    base_path: str = absence.mount_base_path('/absence-reasons/{}')
    urn = base_path.format(absence_reason_id)

    absence_reason.validate_object(absence_reason.kwargs)

    return absence.post(urn=urn, data=absence_reason.__dict__())


def get_all_absences_reasons(absence: Absence):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_absence-reasons&endpoint=rest_query
    :param absence:
    :return:
    """
    urn: str = absence.mount_base_path('/absence-reasons')

    return absence.get(urn=urn)


def get_absences_reason(absence: Absence, absence_reason: str):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_absence-reasons&endpoint=rest_get_xxx
    :param absence:
    :param absence_reason:
    :return:
    """
    base_path: str = absence.mount_base_path('/absence-reasons/{}')
    urn = base_path.format(absence_reason)

    return absence.get(urn=urn)


def delete_absences_reason(absence: Absence, absence_reason: str, params=None):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences_absence-reasons&endpoint=rest_delete_xxx
    :param params:
    :param absence:
    :param absence_reason:
    :return:
    """

    if params is None:
        params = {}

    base_path: str = absence.mount_base_path('/absence-reasons/{}')
    urn = base_path.format(absence_reason)

    available_args: dict = {
        'delete': str
    }

    params = validate(params, available_args)

    return absence.delete(urn=urn, params=params)
