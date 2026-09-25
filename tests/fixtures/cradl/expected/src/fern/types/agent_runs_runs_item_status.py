

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunsRunsItemStatus(enum.StrEnum):
    ARCHIVED = "archived"
    EXPORTED = "exported"
    PENDING_EXPORT = "pending-export"
    PENDING_PREDICTIONS = "pending-predictions"
    READY_FOR_REVIEW = "ready-for-review"
    REVIEW_COMPLETED = "review-completed"
    SUCCEEDED_PREDICTIONS = "succeeded-predictions"
    ERROR = "error"
    RUNNING = "running"
    COMPLETED = "completed"
    REVIEW_IN_PROGRESS = "review-in-progress"

    def visit(
        self,
        archived: typing.Callable[[], T_Result],
        exported: typing.Callable[[], T_Result],
        pending_export: typing.Callable[[], T_Result],
        pending_predictions: typing.Callable[[], T_Result],
        ready_for_review: typing.Callable[[], T_Result],
        review_completed: typing.Callable[[], T_Result],
        succeeded_predictions: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        review_in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgentRunsRunsItemStatus.ARCHIVED:
            return archived()
        if self is AgentRunsRunsItemStatus.EXPORTED:
            return exported()
        if self is AgentRunsRunsItemStatus.PENDING_EXPORT:
            return pending_export()
        if self is AgentRunsRunsItemStatus.PENDING_PREDICTIONS:
            return pending_predictions()
        if self is AgentRunsRunsItemStatus.READY_FOR_REVIEW:
            return ready_for_review()
        if self is AgentRunsRunsItemStatus.REVIEW_COMPLETED:
            return review_completed()
        if self is AgentRunsRunsItemStatus.SUCCEEDED_PREDICTIONS:
            return succeeded_predictions()
        if self is AgentRunsRunsItemStatus.ERROR:
            return error()
        if self is AgentRunsRunsItemStatus.RUNNING:
            return running()
        if self is AgentRunsRunsItemStatus.COMPLETED:
            return completed()
        if self is AgentRunsRunsItemStatus.REVIEW_IN_PROGRESS:
            return review_in_progress()
