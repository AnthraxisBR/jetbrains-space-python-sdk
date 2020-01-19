from tests.base_test_class import TestBase
from space_sdk_ok.space.space import Space


class TestAbsencesAbsenceReason(TestBase):

    def test_mount_base_path(self):

        space_base = Space()

        urn = space_base.mount_base_path('/test')

        self.assertEquals('/api/http/test', urn)
