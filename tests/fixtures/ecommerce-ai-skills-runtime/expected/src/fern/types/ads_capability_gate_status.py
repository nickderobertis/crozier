

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsCapabilityGateStatus(enum.StrEnum):
    CHECKING = "checking"
    PASSED = "passed"
    BLOCKED = "blocked"
    FAILED = "failed"

    def visit(
        self,
        checking: typing.Callable[[], T_Result],
        passed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdsCapabilityGateStatus.CHECKING:
            return checking()
        if self is AdsCapabilityGateStatus.PASSED:
            return passed()
        if self is AdsCapabilityGateStatus.BLOCKED:
            return blocked()
        if self is AdsCapabilityGateStatus.FAILED:
            return failed()
