from space import *

projects = Projects()

response = add_administrator(projects, projectId='lt-integ', profileId='teste')
print(response)