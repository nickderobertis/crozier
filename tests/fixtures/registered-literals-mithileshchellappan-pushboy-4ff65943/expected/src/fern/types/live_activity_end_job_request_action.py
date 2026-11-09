

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LiveActivityEndJobRequestAction(enum.StrEnum):
    END = "end"

    def visit(self, end: typing.Callable[[], T_Result]) -> T_Result:
        if self is LiveActivityEndJobRequestAction.END:
            return end()
