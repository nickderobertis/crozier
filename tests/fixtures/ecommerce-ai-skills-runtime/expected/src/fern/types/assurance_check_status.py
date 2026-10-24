

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssuranceCheckStatus(enum.StrEnum):
    PASSED = "passed"
    FAILED = "failed"
    BLOCKED = "blocked"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssuranceCheckStatus.PASSED:
            return passed()
        if self is AssuranceCheckStatus.FAILED:
            return failed()
        if self is AssuranceCheckStatus.BLOCKED:
            return blocked()
