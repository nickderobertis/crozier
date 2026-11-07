

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineListWorkflowsResponseItemsItemStatus(enum.StrEnum):
    """
    The current status of the workflow.
    """

    SUCCESS = "success"
    RUNNING = "running"
    NOT_RUN = "not_run"
    FAILED = "failed"
    ERROR = "error"
    FAILING = "failing"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"
    UNAUTHORIZED = "unauthorized"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        not_run: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        failing: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        unauthorized: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineListWorkflowsResponseItemsItemStatus.SUCCESS:
            return success()
        if self is PipelineListWorkflowsResponseItemsItemStatus.RUNNING:
            return running()
        if self is PipelineListWorkflowsResponseItemsItemStatus.NOT_RUN:
            return not_run()
        if self is PipelineListWorkflowsResponseItemsItemStatus.FAILED:
            return failed()
        if self is PipelineListWorkflowsResponseItemsItemStatus.ERROR:
            return error()
        if self is PipelineListWorkflowsResponseItemsItemStatus.FAILING:
            return failing()
        if self is PipelineListWorkflowsResponseItemsItemStatus.ON_HOLD:
            return on_hold()
        if self is PipelineListWorkflowsResponseItemsItemStatus.CANCELED:
            return canceled()
        if self is PipelineListWorkflowsResponseItemsItemStatus.UNAUTHORIZED:
            return unauthorized()
