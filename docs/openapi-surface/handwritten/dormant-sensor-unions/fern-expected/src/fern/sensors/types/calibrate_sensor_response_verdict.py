

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CalibrateSensorResponseVerdict(enum.StrEnum):
    PASSED = "passed"
    FAILED = "failed"

    def visit(self, passed: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CalibrateSensorResponseVerdict.PASSED:
            return passed()
        if self is CalibrateSensorResponseVerdict.FAILED:
            return failed()
