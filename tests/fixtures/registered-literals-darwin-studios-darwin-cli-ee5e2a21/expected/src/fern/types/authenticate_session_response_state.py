

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticateSessionResponseState(enum.StrEnum):
    REQUIRED = "required"
    CONNECTED = "connected"

    def visit(self, required: typing.Callable[[], T_Result], connected: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticateSessionResponseState.REQUIRED:
            return required()
        if self is AuthenticateSessionResponseState.CONNECTED:
            return connected()
