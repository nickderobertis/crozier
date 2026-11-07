

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V2WorkflowGetJobResponseStatus(enum.StrEnum):
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
        if self is V2WorkflowGetJobResponseStatus.PENDING:
            return pending()
        if self is V2WorkflowGetJobResponseStatus.PROCESSING:
            return processing()
        if self is V2WorkflowGetJobResponseStatus.COMPLETED:
            return completed()
        if self is V2WorkflowGetJobResponseStatus.FAILED:
            return failed()
