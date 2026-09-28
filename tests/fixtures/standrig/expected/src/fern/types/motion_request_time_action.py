

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionRequestTimeAction(enum.StrEnum):
    SEEK = "seek"

    def visit(self, seek: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionRequestTimeAction.SEEK:
            return seek()
