

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OffRampPropertiesDirection(enum.StrEnum):
    OFF_RAMP = "OffRamp"

    def visit(self, off_ramp: typing.Callable[[], T_Result]) -> T_Result:
        if self is OffRampPropertiesDirection.OFF_RAMP:
            return off_ramp()
