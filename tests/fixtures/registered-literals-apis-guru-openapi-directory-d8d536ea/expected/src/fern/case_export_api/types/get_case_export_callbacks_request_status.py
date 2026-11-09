

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCaseExportCallbacksRequestStatus(enum.StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILURE = "FAILURE"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCaseExportCallbacksRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is GetCaseExportCallbacksRequestStatus.COMPLETE:
            return complete()
        if self is GetCaseExportCallbacksRequestStatus.FAILURE:
            return failure()
