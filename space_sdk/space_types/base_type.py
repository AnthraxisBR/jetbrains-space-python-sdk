from space_sdk.space_types.check_types import (
    validate_object
)
from space_sdk.exceptions.TypeException import InvalidObjectException

class BaseType(object):

    validated_dict : dict


    def validate_object(self):
        self.validated_dict : dict = validate_object(self)

    def only_available_attrs(self, attrs: list):
        if any(item in self.validated_dict for item in attrs):
            error_str: str = ', '.join(attrs)
            raise InvalidObjectException(errors=[
                'Doesn\'t use any of these fields ({}) when creating checklist'.format(error_str)])

    def not_allowed_attr(self, attr: str):
        if attr in self.validated_dict:
            raise InvalidObjectException(errors=['Doesn\'t use field {} value when updating checklist'.format(attr)])