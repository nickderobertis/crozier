

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InsightsGetRecentWorkflowRunsResponseItemsItemStatus(enum.StrEnum):
    """
    Workflow status.
    """

    SUCCESS = "success"
    FAILED = "failed"
    ERROR = "error"
    CANCELED = "canceled"
    UNAUTHORIZED = "unauthorized"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InsightsGetRecentWorkflowRunsResponseItemsItemStatus.SUCCESS:
            return success()
        if self is InsightsGetRecentWorkflowRunsResponseItemsItemStatus.FAILED:
            return failed()
        if self is InsightsGetRecentWorkflowRunsResponseItemsItemStatus.ERROR:
            return error()
        if self is InsightsGetRecentWorkflowRunsResponseItemsItemStatus.CANCELED:
            return canceled()
        if self is InsightsGetRecentWorkflowRunsResponseItemsItemStatus.UNAUTHORIZED:
            return unauthorized()
