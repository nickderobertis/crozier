

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentRunStatus(enum.StrEnum):
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
        if self is AgentRunStatus.ARCHIVED:
            return archived()
        if self is AgentRunStatus.EXPORTED:
            return exported()
        if self is AgentRunStatus.PENDING_EXPORT:
            return pending_export()
        if self is AgentRunStatus.PENDING_PREDICTIONS:
            return pending_predictions()
        if self is AgentRunStatus.READY_FOR_REVIEW:
            return ready_for_review()
        if self is AgentRunStatus.REVIEW_COMPLETED:
            return review_completed()
        if self is AgentRunStatus.SUCCEEDED_PREDICTIONS:
            return succeeded_predictions()
        if self is AgentRunStatus.ERROR:
            return error()
        if self is AgentRunStatus.RUNNING:
            return running()
        if self is AgentRunStatus.COMPLETED:
            return completed()
        if self is AgentRunStatus.REVIEW_IN_PROGRESS:
            return review_in_progress()
