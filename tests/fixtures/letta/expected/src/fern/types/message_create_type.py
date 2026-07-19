

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageCreateType(enum.StrEnum):
    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageCreateType.MESSAGE:
            return message()
