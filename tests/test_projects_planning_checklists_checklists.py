import settings
import unittest
from tests.base_test_class import TestBase
from space import *


class TestProjectsPlanningChecklistChecklists(object):

    projects: Projects

    def setUp(self) -> None:
        self.projects = Projects()
        super(TestProjectsPlanningChecklistChecklists, self).setUp()

    def test_create_checklist(self):
        checklist = Checklist(name='Teste', projectId='space-sdk')
        response = create_checklist(self.projects, checklist)
        self.assertEqual(response.status_code, 200)

    def test_get_all_checklists(self):
        response = get_all_checklists(self.projects, 'space-sdk')
        print(response)
        print(response.content)
        self.assertEqual(response.status_code, 200)


#if __name__ == '__main__':
 #   unittest.main()


checklist = Checklist(name='Teste 2')#, projectId='asdsad')

print(update_checklist(Projects(), checklistId='3rn8DT2PlXEr', checklist=checklist))