# jetbrains-space-python-sdk

Jetbrains Space Python SDK (under development)

# Generate a Access Token: 

1. Fill .env with your space data
2. Call helper/generate_space_authorization_code.py
3. Follow instructions to generate your access token

# Use: 
    
Set SPACE_ACCESS_TOKEN in your project .env:
    
To import all methods:

    from space import *

To import only specific module:

    from space.project import *
    
To import only one specific method:
    
    from space.project.administrators.members import add_administrator

# Example of call:

    from space.project.administrators.members import add_administrator
    projects = Projects()
    response = add_administrator(projects, projectId='your-project-id', profileId='your-profile-id')

#TODO
1. Auto refresh token
2. Most part of routes
3. Implement Tests
4. Tutorial

