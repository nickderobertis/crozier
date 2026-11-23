

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RampDirection(enum.StrEnum):
    ON_RAMP = "OnRamp"

    def visit(self, on_ramp: typing.Callable[[], T_Result]) -> T_Result:
        if self is RampDirection.ON_RAMP:
            return on_ramp()
