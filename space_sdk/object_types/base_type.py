import inspect
from ..space_types.custom_types import Empty

from ..space_types.check_types import (
    is_nullable,
    validation_messages,
    required
)

from ..exceptions.TypeException import (
    InvalidObjectException
)


class BaseType(object):
    annotations: list

    attributes: list

    kwargs: dict

    validated_attrs: dict

    def serialize_annotations(self):
        print(self.annotations)
        print(self.kwargs)

        for arg in self.kwargs:
            if arg in self.annotations:
                print(self.annotations[arg])

    def __dict__(self):
        dict_response: dict = {}
        for attr in self.validated_attrs:
            if issubclass(type(self.validated_attrs[attr]), RequestType):
                dict_response[attr] = self.validated_attrs[attr].__dict__()
            else:
                dict_response[attr] = self.validated_attrs[attr]
        return dict_response

    def __str__(self):
        return str(self.validated_attrs)


class RequestType(BaseType):

    def __init__(self, **kwargs):
        self.validated_dict = None
        self.attributes: dict = self.__class__.__dict__
        self.validate_object(kwargs)

    def validate_object(self, kwargs):
        errors: list = []
        validated_attrs: dict = {}
        attrs: list = [a for a in dir(self) if not a.startswith('__')]
        for attr in attrs:
            approved: bool = False
            cls_attrs = getattr(self, attr)
            if inspect.ismethod(cls_attrs):
                continue

            for rule in cls_attrs:

                if not callable(rule) or rule == Empty:
                    continue

                if required in cls_attrs and attr not in kwargs:
                    errors.append(validation_messages[rule].format(attr, self.__class__.__name__))
                    continue

                if required not in cls_attrs and attr not in kwargs:
                    continue

                # if issubclass(type(self), RequestType):
                #     print(attr)
                #     validated_attrs[attr] = kwargs[attr]
                #     continue

                if not rule(kwargs[attr]) and is_nullable not in cls_attrs:
                    if rule in validation_messages:
                        errors.append(validation_messages[rule].format(attr, self.__class__.__name__))
                else:
                    approved: bool = True

                if approved:
                    validated_attrs[attr] = kwargs[attr]
        if len(errors) > 0:
            raise InvalidObjectException(errors=errors)

        self.validated_attrs = validated_attrs

    def get_validated_attrs(self):
        return self.validated_attrs

    def only_available_attrs(self, attrs: list):
        if any(item in self.validated_dict for item in attrs):
            error_str: str = ', '.join(attrs)
            raise InvalidObjectException(errors=[
                'Doesn\'t use any of these fields ({}) when creating checklist'.format(error_str)])

    def not_allowed_attr(self, attr: str):
        if attr in self.validated_dict:
            raise InvalidObjectException(errors=['Doesn\'t use field {} value when updating checklist'.format(attr)])


class RecordType(BaseType):

    def __init__(self, **kwargs):
        self.annotations: dict = self.__class__.__annotations__
        self.kwargs: dict = kwargs
        self.serialize_annotations()
        self.__dict__.update(kwargs)

    def serialize(self):
        pass


