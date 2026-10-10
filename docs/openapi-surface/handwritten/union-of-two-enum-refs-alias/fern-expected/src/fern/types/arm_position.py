

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArmPosition(enum.StrEnum):
    RAISED = "raised"
    LOWERED = "lowered"

    def visit(self, raised: typing.Callable[[], T_Result], lowered: typing.Callable[[], T_Result]) -> T_Result:
        if self is ArmPosition.RAISED:
            return raised()
        if self is ArmPosition.LOWERED:
            return lowered()
