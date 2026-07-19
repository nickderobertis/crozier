

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StepStatus(enum.StrEnum):
    """
    Status of a step execution
    """

    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StepStatus.PENDING:
            return pending()
        if self is StepStatus.SUCCESS:
            return success()
        if self is StepStatus.FAILED:
            return failed()
        if self is StepStatus.CANCELLED:
            return cancelled()
