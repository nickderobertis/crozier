

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TestExecutionStatus(enum.StrEnum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    PASSED = "PASSED"
    FAILED = "FAILED"
    NOT_TESTED = "NOT_TESTED"
    ENDED_PREMATURELY = "ENDED_PREMATURELY"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        not_tested: typing.Callable[[], T_Result],
        ended_prematurely: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestExecutionStatus.NOT_STARTED:
            return not_started()
        if self is TestExecutionStatus.IN_PROGRESS:
            return in_progress()
        if self is TestExecutionStatus.PASSED:
            return passed()
        if self is TestExecutionStatus.FAILED:
            return failed()
        if self is TestExecutionStatus.NOT_TESTED:
            return not_tested()
        if self is TestExecutionStatus.ENDED_PREMATURELY:
            return ended_prematurely()
