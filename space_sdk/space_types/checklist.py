from space_sdk.space_types import *
from space_sdk.space_types import Empty
from space_sdk.space_types.check_types import (
    is_nullable, required, is_str, validate_object
)
from space_sdk.exceptions.TypeException import InvalidObjectException


class Checklist(object):
    projectId: list = [is_nullable]

    name: list = [required, is_str]

    description: list = [is_nullable, is_str]

    owner: list = [is_nullable, is_str]

    tag: list = [is_nullable, is_str]

    def __init__(self, name: str = Empty, projectId=Empty, owner: str = Empty, tag: str = Empty, description: str = Empty):
        self.projectId.append(projectId)
        self.name.append(name)
        self.owner.append(owner)
        self.tag.append(tag)
        self.description.append(description)

    def __todict__(self, kind=None):
        validated_dict : dict = validate_object(self)
        if kind is None or kind == 'create':
            if any(item in validated_dict for item in ['description', 'owner','tag']):
                raise InvalidObjectException(errors=['Doesn\'t use any of these fields (\'description\', \'owner\',\'tag\') when creating checklist'])
            return validated_dict
        elif kind == 'update':
            if 'projectId' in validated_dict:
                raise InvalidObjectException(errors=['Doesn\'t use field projectId value when updating checklist'])
            return validated_dict
