

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageInputKind(enum.StrEnum):
    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageInputKind.MESSAGE:
            return message()
