from space_sdk.object_types.absence.absence_reason import AbsencesAbsenceReasonRequest
from space_sdk.space.absence.absence import Absence


def create_reason_absence(absence: Absence, absence_reason: AbsencesAbsenceReasonRequest):
    """
        https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_update_xxx
    :param absence:
    :param absence_reason:
    :return:
    """
    base_path: str = absence.mount_base_path('absence-reasons')
    urn = base_path.format(absence.absence)

    absence_reason.validate_object(absence_reason.__dict__())

    return absence.post(urn=urn, data=absence_reason.get_validated_attrs())
