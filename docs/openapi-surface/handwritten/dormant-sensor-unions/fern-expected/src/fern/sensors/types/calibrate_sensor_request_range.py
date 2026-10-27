

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CalibrateSensorRequestRange(enum.StrEnum):
    SHORT = "short"
    LONG = "long"

    def visit(self, short: typing.Callable[[], T_Result], long_: typing.Callable[[], T_Result]) -> T_Result:
        if self is CalibrateSensorRequestRange.SHORT:
            return short()
        if self is CalibrateSensorRequestRange.LONG:
            return long_()
