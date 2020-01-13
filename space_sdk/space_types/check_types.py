import pendulum
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


def is_list(value):
    return type(value) == list


def is_bool(value):
    return type(value) == bool


def is_float(value):
    return type(value) == float


def is_nullable(value):
    return value is None


def required(value):
    return value is not None and value is not Empty


def is_date(value):
    try:
        pendulum.pase(value)
    except Exception as e:
        return False
    return True


def is_list_of(value, of_type: BaseType):
    for value_item in value:
        if not (type(value_item) == type(of_type)):
            return False


validation_messages = {
    is_str: 'Field "{}" must be type of string',
    is_int: 'Field "{}" must be type of integer',
    is_float: 'Field "{}" must be type of float',
    required: 'Field "{}" is required',
    is_date: 'Field "{}" must be a valid date in format Y-m-d',
    is_list_of: 'Field "{}" must a list'
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
        if isinstance(value, BaseType):
            pass
        g
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
