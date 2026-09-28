

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2LogListItemStatus(enum.StrEnum):
    """
    Current execution status, reported as persisted. `redacting` is transient while run output is scrubbed. `paused` is reported only when a resume attempt did not complete; a run held at a human-in-the-loop pause point reads `pending` here, and `paused` on the workflow run resources. Use those when the pause state matters.
    """

    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    REDACTING = "redacting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        redacting: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2LogListItemStatus.PENDING:
            return pending()
        if self is V2LogListItemStatus.RUNNING:
            return running()
        if self is V2LogListItemStatus.PAUSED:
            return paused()
        if self is V2LogListItemStatus.REDACTING:
            return redacting()
        if self is V2LogListItemStatus.COMPLETED:
            return completed()
        if self is V2LogListItemStatus.FAILED:
            return failed()
        if self is V2LogListItemStatus.CANCELLED:
            return cancelled()
