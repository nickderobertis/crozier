

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdsCapabilityGateChecksItemStatus(enum.StrEnum):
    PASSED = "passed"
    BLOCKED = "blocked"
    FAILED = "failed"
    SKIPPED = "skipped"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdsCapabilityGateChecksItemStatus.PASSED:
            return passed()
        if self is AdsCapabilityGateChecksItemStatus.BLOCKED:
            return blocked()
        if self is AdsCapabilityGateChecksItemStatus.FAILED:
            return failed()
        if self is AdsCapabilityGateChecksItemStatus.SKIPPED:
            return skipped()
