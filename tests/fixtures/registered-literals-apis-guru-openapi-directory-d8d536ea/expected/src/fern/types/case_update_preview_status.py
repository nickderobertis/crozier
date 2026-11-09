

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseUpdatePreviewStatus(enum.StrEnum):
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
        if self is CaseUpdatePreviewStatus.COMPLETE:
            return complete()
        if self is CaseUpdatePreviewStatus.FAILURE:
            return failure()
        if self is CaseUpdatePreviewStatus.IN_PROGRESS:
            return in_progress()
