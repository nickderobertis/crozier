

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStopped(enum.StrEnum):
    """
    Why the job stopped.
    """

    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    def visit(self, cancelled: typing.Callable[[], T_Result], completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobStopped.CANCELLED:
            return cancelled()
        if self is JobStopped.COMPLETED:
            return completed()
