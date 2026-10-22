

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSingleMessageResponseStatus(enum.StrEnum):
    """
    Status of the message
    """

    QUEUED = "queued"
    SCHEDULED = "scheduled"
    ERROR = "error"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSingleMessageResponseStatus.QUEUED:
            return queued()
        if self is CreateSingleMessageResponseStatus.SCHEDULED:
            return scheduled()
        if self is CreateSingleMessageResponseStatus.ERROR:
            return error()
