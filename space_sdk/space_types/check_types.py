import inspect
from space_sdk.space_types import *
from space_sdk.exceptions.TypeException import InvalidParameterTypeException, InvalidObjectException

def validate(params: dict, comparable: dict):
    filtered_params: dict = {}
    for index, param in enumerate(params):
        if param in params:
            if not (type(params[param]) == comparable[param]):
                raise InvalidParameterTypeException(param, comparable[param])
            else:
                filtered_params[param] = params[param]
    return filtered_params


def is_str(value):
    return type(value) == str


def is_int(value):
    return type(value) == int


def is_float(value):
    return type(value) == float


def is_nullable(value):
    return value is None


def required(value):
    return value is not None and value is not Empty


validation_messages = {
    is_str: 'Field "{}" must type of string',
    is_int: 'Field "{}" must type of integer',
    is_float: 'Field "{}" must type of float',
    required: 'Field "{}" is required'
}


def check_validation_function(attr, value, func_list) -> list:
    checks: list = []
    for func in func_list:
        if not callable(func) or func == Empty:
            continue

        if not func(value) and is_nullable not in func_list:
            if func in validation_messages:
                checks.append(validation_messages[func].format(attr))
    return checks


def validate_object(obj):
    attrs: list = [a for a in dir(obj) if not a.startswith('__')]

    errors: list = []
    new_dict: dict = {}
    for attr in attrs:

        cls_attr = getattr(obj, attr)
        if inspect.ismethod(cls_attr):
            continue

        value = cls_attr[len(cls_attr) - 1]
        checks = check_validation_function(attr, value, cls_attr)
        if len(checks) > 0:
            errors += checks
        else:
            if value is not Empty:
                new_dict[attr] = value

    if len(errors) > 0:
        print(errors)
        raise InvalidObjectException(errors=errors)
    return new_dict
