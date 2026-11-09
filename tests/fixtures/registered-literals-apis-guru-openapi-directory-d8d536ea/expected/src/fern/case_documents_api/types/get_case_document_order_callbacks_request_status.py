

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCaseDocumentOrderCallbacksRequestStatus(enum.StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETE = "COMPLETE"
    FAILURE = "FAILURE"

    def visit(
        self,
        in_progress: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCaseDocumentOrderCallbacksRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is GetCaseDocumentOrderCallbacksRequestStatus.COMPLETE:
            return complete()
        if self is GetCaseDocumentOrderCallbacksRequestStatus.FAILURE:
            return failure()
