from pendulum import date
from ...typing.consts import viewMode
from ...typing.check_types import validate
from ...typing.absence.absence import (
    AbsenceRequest,
    ApproveAbsenceRequest
)
from ..space import Space


class Absence(Space):
    project: str

    def __init__(self, absence=None):
        urn: str = '/absences'

        super(Absence, self).__init__()

        self.absence: str = absence

        self.urn += urn


def create_absence(absence: Absence, absence_request: AbsenceRequest):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_create
        :param absence:
        :param absence_request:
        :return:
        """

    urn: str = absence.urn

    absence_request.validate_object(absence_request.kwargs)

    return absence.post(urn=urn, data=absence_request.__dict__())


def get_all_absences(absence: Absence, params=None):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_create
        :param absence:
        :param params:
        :return:
        """

    if params is None:
        params = {}

    available_args: dict = {
        '$skip': str,  # str?
        '$top': int,  # int?
        'member': str,  # CodeReviewState?
        'location': str,  # string?
        'team': str,  # string?
        'since': date,
        'till': date,  # string?
        'viewMode': viewMode,  # viewMode
    }

    params = validate(params, available_args)

    urn: str = absence.urn

    return absence.get(urn=urn, params=params)


def get_all_absences_by_member(absence: Absence, member: str):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_query_member%3Axxx
        :param absence:
        :param member:
        :return:
        """

    base_path: str = absence.mount_base_path('/member:{}')
    urn: str = base_path.format(member)

    return absence.get(urn=urn)


def get_absence(absence: Absence, absence_id: str):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_get_xxx
        :param absence:
        :param absence_id:
        :return:
        """

    base_path: str = absence.mount_base_path('/{}')
    urn: str = base_path.format(absence_id)

    return absence.get(urn=urn)


def update_absence(absence: Absence, absence_id: str, absence_request: AbsenceRequest):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_update_xxx
        :param absence:
        :param absence_id:
        :param absence_request:
        :return:
        """

    base_path: str = absence.mount_base_path('/{}')
    urn: str = base_path.format(absence_id)

    absence_request.validate_object(absence_request.kwargs)

    return absence.patch(urn=urn, data=absence_request.__dict__())


def delete_absence(absence: Absence, absence_id: str):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=rest_delete_xxx
        :param absence:
        :param absence_id:
        :return:
        """

    base_path: str = absence.mount_base_path('/{}')
    urn: str = base_path.format(absence_id)

    return absence.delete(urn=urn)


def approve_absence(absence: Absence, absence_id: str, approve_absence: ApproveAbsenceRequest):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=http_post_xxx_approve
        :param absence:
        :param absence_id:
        :param approve_absence:
        :return:
        """

    base_path: str = absence.mount_base_path('/{}/approve')
    urn: str = base_path.format(absence_id)

    approve_absence.validate_object(approve_absence.kwargs)

    return absence.post(urn=urn, data=approve_absence.__dict__())


def delete_absence_approval(absence: Absence, absence_id: str):
    """
            https://{company}.jetbrains.space/httpApiPlayground?resource=absences&endpoint=http_delete_xxx_delete-approval
        :param absence:
        :param absence_id:
        :param approve_absence:
        :return:
        """

    base_path: str = absence.mount_base_path('/{}/delete-approval')
    urn: str = base_path.format(absence_id)

    return absence.delete(urn=urn)
