

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseUpdateStatus(enum.StrEnum):
    """
    Status of the request.
    """

    COMPLETE = "COMPLETE"
    FAILURE = "FAILURE"
    IN_PROGRESS = "IN_PROGRESS"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseUpdateStatus.COMPLETE:
            return complete()
        if self is CaseUpdateStatus.FAILURE:
            return failure()
        if self is CaseUpdateStatus.IN_PROGRESS:
            return in_progress()
