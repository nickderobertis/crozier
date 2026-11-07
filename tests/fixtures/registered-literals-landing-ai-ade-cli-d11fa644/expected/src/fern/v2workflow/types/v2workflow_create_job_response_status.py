

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V2WorkflowCreateJobResponseStatus(enum.StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2WorkflowCreateJobResponseStatus.PENDING:
            return pending()
        if self is V2WorkflowCreateJobResponseStatus.PROCESSING:
            return processing()
        if self is V2WorkflowCreateJobResponseStatus.COMPLETED:
            return completed()
        if self is V2WorkflowCreateJobResponseStatus.FAILED:
            return failed()
