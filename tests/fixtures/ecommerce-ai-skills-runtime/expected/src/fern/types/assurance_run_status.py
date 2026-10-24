

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssuranceRunStatus(enum.StrEnum):
    RUNNING = "running"
    PASSED = "passed"
    FAILED = "failed"
    BLOCKED = "blocked"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssuranceRunStatus.RUNNING:
            return running()
        if self is AssuranceRunStatus.PASSED:
            return passed()
        if self is AssuranceRunStatus.FAILED:
            return failed()
        if self is AssuranceRunStatus.BLOCKED:
            return blocked()
