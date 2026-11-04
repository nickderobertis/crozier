

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActEndActionResponseType(enum.StrEnum):
    END = "end"

    def visit(self, end: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActEndActionResponseType.END:
            return end()
