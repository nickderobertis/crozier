

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCallbacksRequestStatus(enum.StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILURE = "FAILURE"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCallbacksRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is GetCallbacksRequestStatus.COMPLETE:
            return complete()
        if self is GetCallbacksRequestStatus.FAILURE:
            return failure()
