from build.lib.space import *
from build.lib.space_types import *


checklist = Checklist(name='Teste 2')#, projectId='asdsad')

print(update_checklist(Projects(), checklistId='', checklist=checklist))


get_all_checklists()