

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionState(str, enum.Enum):
    """
    [Connection state flow](#section/Connection-state)
    """

    AVAILABLE = "available"
    CALLABLE = "callable"
    ADDED = "added"
    AUTHORIZED = "authorized"
    INVALID = "invalid"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        callable: typing.Callable[[], T_Result],
        added: typing.Callable[[], T_Result],
        authorized: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionState.AVAILABLE:
            return available()
        if self is ConnectionState.CALLABLE:
            return callable()
        if self is ConnectionState.ADDED:
            return added()
        if self is ConnectionState.AUTHORIZED:
            return authorized()
        if self is ConnectionState.INVALID:
            return invalid()
