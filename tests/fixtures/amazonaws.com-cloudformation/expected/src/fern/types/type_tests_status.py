

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypeTestsStatus(str, enum.Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_TESTED = "NOT_TESTED"

    def visit(
        self,
        passed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        not_tested: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypeTestsStatus.PASSED:
            return passed()
        if self is TypeTestsStatus.FAILED:
            return failed()
        if self is TypeTestsStatus.IN_PROGRESS:
            return in_progress()
        if self is TypeTestsStatus.NOT_TESTED:
            return not_tested()
