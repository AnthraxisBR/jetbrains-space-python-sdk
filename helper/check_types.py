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

