

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionAttemptStatus(enum.StrEnum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    INDETERMINATE = "indeterminate"

    def visit(
        self,
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        indeterminate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExtractionAttemptStatus.SUCCEEDED:
            return succeeded()
        if self is ExtractionAttemptStatus.FAILED:
            return failed()
        if self is ExtractionAttemptStatus.INDETERMINATE:
            return indeterminate()
