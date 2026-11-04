

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParseCreateJobResponseStatus(enum.StrEnum):
    """
    The job's status at creation — normally ``pending`` (a just-created job that is still running is reported as ``pending``), but may already be a terminal ``completed`` / ``failed`` if the job finished before the create response was rendered.
    """

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
        if self is ParseCreateJobResponseStatus.PENDING:
            return pending()
        if self is ParseCreateJobResponseStatus.PROCESSING:
            return processing()
        if self is ParseCreateJobResponseStatus.COMPLETED:
            return completed()
        if self is ParseCreateJobResponseStatus.FAILED:
            return failed()
