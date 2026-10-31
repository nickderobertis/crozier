

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TestResultStatus(enum.StrEnum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestResultStatus.PASSED:
            return passed()
        if self is TestResultStatus.FAILED:
            return failed()
        if self is TestResultStatus.SKIPPED:
            return skipped()
