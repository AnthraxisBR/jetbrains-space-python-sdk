import inspect
import pendulum
from ..exceptions.TypeException import InvalidParameterTypeException
from .custom_types import Empty


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
        pendulum.parse(value)
    except Exception as e:
        return False
    return True


validation_messages = {
    is_str: 'Field "{}" must be type of string in object {}',
    is_int: 'Field "{}" must be type of integer in object {}',
    is_float: 'Field "{}" must be type of float in object {}',
    is_bool: 'Field "{}" must be type of boolean in object {}',
    required: 'Field "{}" is required in object {}',
    is_date: 'Field "{}" must be a valid date in format Y-m-d in object {}',
}

