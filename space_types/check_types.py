from space_types import *
from exceptions.TypeException import InvalidParameterTypeException


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
    return value is not None


validation_messages = {
    is_str: 'Field {} must type of string',
    is_int: 'Field {} must type of integer',
    is_float: 'Field {} must type of float',
    required: 'Field {} is required '
}


def check_validation_function(attr, value, func_list):
    checks: list = []
    for func in func_list:
        if not callable(func) or func == Empty:
            continue

        if not func(value):
            if func in validation_messages:
                checks.append(validation_messages[func])
    print(checks)
