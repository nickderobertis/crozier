

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MotionRequestLoopAction(enum.StrEnum):
    CONFIGURE = "configure"

    def visit(self, configure: typing.Callable[[], T_Result]) -> T_Result:
        if self is MotionRequestLoopAction.CONFIGURE:
            return configure()
