

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalResourcesSharedModelsTranslationRequestState(enum.StrEnum):
    """
    The state of the request
    """

    NOT_SUBMITTED = "NotSubmitted"
    SUBMITTED = "Submitted"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"

    def visit(
        self,
        not_submitted: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalResourcesSharedModelsTranslationRequestState.NOT_SUBMITTED:
            return not_submitted()
        if self is GlobalResourcesSharedModelsTranslationRequestState.SUBMITTED:
            return submitted()
        if self is GlobalResourcesSharedModelsTranslationRequestState.CANCELLED:
            return cancelled()
        if self is GlobalResourcesSharedModelsTranslationRequestState.COMPLETED:
            return completed()
