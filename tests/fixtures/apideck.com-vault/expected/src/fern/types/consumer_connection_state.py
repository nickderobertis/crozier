

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConsumerConnectionState(str, enum.Enum):
    AVAILABLE = "available"
    CALLABLE = "callable"
    ADDED = "added"
    CONFIGURED = "configured"
    AUTHORIZED = "authorized"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        callable: typing.Callable[[], T_Result],
        added: typing.Callable[[], T_Result],
        configured: typing.Callable[[], T_Result],
        authorized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsumerConnectionState.AVAILABLE:
            return available()
        if self is ConsumerConnectionState.CALLABLE:
            return callable()
        if self is ConsumerConnectionState.ADDED:
            return added()
        if self is ConsumerConnectionState.CONFIGURED:
            return configured()
        if self is ConsumerConnectionState.AUTHORIZED:
            return authorized()
