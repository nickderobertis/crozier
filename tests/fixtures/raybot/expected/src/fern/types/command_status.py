

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommandStatus(enum.StrEnum):
    """
    The status of the command
    """

    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    CANCELING = "CANCELING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        canceling: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommandStatus.QUEUED:
            return queued()
        if self is CommandStatus.PROCESSING:
            return processing()
        if self is CommandStatus.CANCELING:
            return canceling()
        if self is CommandStatus.SUCCEEDED:
            return succeeded()
        if self is CommandStatus.FAILED:
            return failed()
        if self is CommandStatus.CANCELED:
            return canceled()
