import unittest
from tests.base_test_class import TestBase
from space_sdk_ok.space.absence.absence import Absence
from space_sdk_ok.space.absence.absence_reason import (
    create_absence_reason,
    create_absence_reason_in_absence_reason,
    get_all_absence_reasons,
    get_absence_reason,
    delete_absence_reason
)
from space_sdk_ok.typing.absence.absence_reason import AbsencesAbsenceReasonRequest
from space_sdk_ok.exceptions.TypeException import InvalidObjectException


class TestAbsencesAbsenceReason(TestBase):
    absence: Absence

    def setUp(self) -> None:
        self.absence = Absence()
        super(TestAbsencesAbsenceReason, self).setUp()

    def test_create_absence_reason_with_success(self):
        absence_reason = AbsencesAbsenceReasonRequest(
            name='Absence Test',
            description='test description',
            defaultAvailability=True,
            approvalRequired=True,
            icon='icon'
        )

        response = create_absence_reason(self.absence, absence_reason)

        self.assertEqual(response.status_code, 200)

    def test_create_absence_reason_with_invalid_object(self):
        self.assertRaises(
            InvalidObjectException,
            AbsencesAbsenceReasonRequest,
            name='Absence Test',
            description='test description',
            approvalRequired=True
        )

    def test_create_absence_reason_in_absence_reason_with_success(self):
        absence_reason = AbsencesAbsenceReasonRequest(
            name='Absence Test',
            description='test description',
            defaultAvailability=True,
            approvalRequired=True,
            icon='icon'
        )

        response = create_absence_reason_in_absence_reason(self.absence, 'id', absence_reason)

        self.assertEqual(response.status_code, 200)

    def test_get_all_absence_reasons(self):
        response = get_all_absence_reasons(self.absence)

        self.assertEqual(response.status_code, 200)

    def test_get_absence_reasons(self):
        response = get_absence_reason(self.absence, 'id')

        self.assertEqual(response.status_code, 200)

    def test_delete_absence_reason(self):
        response = delete_absence_reason(self.absence, 'id', {
            'delete': 'true'
        })

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
