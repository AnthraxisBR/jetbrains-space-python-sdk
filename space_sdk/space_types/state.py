from space_sdk.space_types.consts import (
    Opened, Closed, Deleted
)
from space_sdk.exceptions.TypeException import InvalidStateException


class State(object):
    states: list = [
        Opened, Closed, Deleted
    ]

    state: str

    def __init__(self, state: str):
        if state not in self.states:
            raise InvalidStateException()
        self.state = state

    def __str__(self):
        return self.state

