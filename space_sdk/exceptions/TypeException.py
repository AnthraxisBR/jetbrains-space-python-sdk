class InvalidStateException(Exception):

    def __init__(self, message: str = 'Space SDK Typing error', errors=None):
        super(Exception, self).__init__(message)

        if errors is None:
            errors = ['Invalid State Value']

        self.errors = errors


class InvalidParameterTypeException(Exception):

    def __init__(self, parameter: str, correct_type: str, message: str = 'Space SDK Typing error', errors=None):
        super(Exception, self).__init__(message)

        if errors is None:
            errors = [f'Invalid URL parameter type: {parameter} has to be type of {correct_type}']

        self.errors = errors


class InvalidObjectException(Exception):

    def __init__(self, message: str = 'Space SDK Object Typing error', errors=None):
        message += ': ' + ', '.join(errors)
        super(Exception, self).__init__(message)

        if errors is None:
            errors = [f'Invalid Object type: undefined type error']

        self.errors = errors
