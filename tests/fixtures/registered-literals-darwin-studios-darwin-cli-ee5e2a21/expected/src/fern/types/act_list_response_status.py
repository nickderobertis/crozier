

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActListResponseStatus(enum.StrEnum):
    COMPLETED = "completed"

    def visit(self, completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActListResponseStatus.COMPLETED:
            return completed()
